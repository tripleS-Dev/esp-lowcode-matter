import requests
from json import loads
from urllib.parse import quote

class SharePointClient:
    def __init__(self, tenant_id, client_id, client_secret, resource):
        self.tenant_id = tenant_id
        self.client_id = client_id
        self.client_secret = client_secret
        self.resource = resource

    def encode_file_path(file_path):
        return quote(file_path)

    def get_access_token(self):
        url = f"https://login.microsoftonline.com/{self.tenant_id}/oauth2/token"
        payload = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'resource': self.resource,
            'grant_type': 'client_credentials'
        }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        try:
            response = requests.post(url, headers=headers, data=payload)
            response.raise_for_status()
            return loads(response.text)['access_token']
        except requests.RequestException as e:
            print(f"Failed to generate access token: {e}")
            if response is not None:
                print("Response content for debugging:", response.text)
            return None

    def get_target_site(self, access_token, site_name='matter'):
        if not access_token:
            return None

        url = "https://graph.microsoft.com/v1.0/sites?search=" + site_name
        headers = {'Authorization': f'Bearer {access_token}'}
        for _ in range(5):
            try:
                response = requests.get(url, headers=headers)
                response.raise_for_status()
                sites = loads(response.text).get('value', [])
                for site in sites:
                    if site['name'] == site_name:
                        return site
                print(f"Target Site '{site_name}' Not Found!")
                return None
            except requests.RequestException:
                sleep(1)  # Retry delay
        print("Connect SharePoint Site Failed: Max 5 retries reached.")
        return None

    def get_target_drive_path(self, site, access_token, drive_name='Documents'):
        if not access_token or not site:
            return None

        site_id = site['id']
        url = f"https://graph.microsoft.com/v1.0/sites/{site_id}/drives"
        headers = {'Authorization': f'Bearer {access_token}'}

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            drives = loads(response.text).get('value', [])
            for drive in drives:
                if drive['name'] == drive_name:
                    return drive
            print(f"Target Drive Path '{drive_name}' Not Found!")
        except requests.RequestException as e:
            print("Failed to get target drive path:", e)
        return None

    def get_target_file(self, site, drive, target_file, access_token):
        if not site or not drive or not target_file or not access_token:
            return None, None

        site_id = site['id']
        drive_id = drive['id']
        encoded_target_file = quote(target_file)  # URL-encoding the file path
        url = f"https://graph.microsoft.com/v1.0/sites/{site_id}/drives/{drive_id}/root:/{encoded_target_file}"
        headers = {'Authorization': f'Bearer {access_token}'}

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            file_info = loads(response.text)
            file_name = file_info.get('name')
            file_url = file_info.get('@microsoft.graph.downloadUrl')
            return file_name, file_url
        except requests.RequestException as e:
            print("Failed to get target file:", e)
            return None, None

    def download_file(self, file_url, filename):
        try:
            response = requests.get(file_url)
            response.raise_for_status()
            with open(filename, "wb") as file:
                file.write(response.content)
            print(f"{filename} saved successfully")
        except requests.RequestException as e:
            print(f"Failed to download {filename}: {e}")

    def run_all(self, target_file):
        token = self.get_access_token()
        site = self.get_target_site(token)
        drive = self.get_target_drive_path(site, token)
        file_name, file_url = self.get_target_file(site, drive, target_file, token)

        if file_name and file_url:
            file_content = download_file(file_url)
            return file_name, file_content
        return None, None

# Function to download content from a URL
def download_file(url: str):
    response = requests.get(url)
    response.raise_for_status()  # Ensure the download was successful
    return response.content

