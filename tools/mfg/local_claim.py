#!/usr/bin/env python3
import os
import sys
import datetime
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography import x509
from cryptography.hazmat.primitives import hashes

def get_vid_from_csr(csr):
    vid_subject = x509.ObjectIdentifier('1.3.6.1.4.1.37244.2.1')
    vid = csr.subject.get_attributes_for_oid(vid_subject)[0].value
    return vid

def get_ca_cert_and_key(certs_path, vid):
    ca_cert_file_name = 'pai_cert_' + vid.lower() + '.pem'
    ca_key_file_name = 'pai_key_' + vid.lower() + '.pem'
    ca_cert_file = os.path.join(certs_path, ca_cert_file_name)
    ca_key_file = os.path.join(certs_path, ca_key_file_name)

    with open(ca_cert_file, 'rb') as f:
        ca_cert = x509.load_pem_x509_certificate(f.read(), default_backend())

    with open(ca_key_file, 'rb') as f:
        ca_key = serialization.load_pem_private_key(f.read(), password=None, backend=default_backend())
    return ca_cert, ca_key

def local_dac_gen(csr_pem, certs_path):
    csr = x509.load_pem_x509_csr(csr_pem.encode('utf-8'), default_backend())
    vid = get_vid_from_csr(csr)
    ca_cert, ca_key = get_ca_cert_and_key(certs_path, vid)

    cert = x509.CertificateBuilder()
    cert = cert.subject_name(csr.subject)
    cert = cert.issuer_name(ca_cert.subject)
    cert = cert.public_key(csr.public_key())
    cert = cert.serial_number(x509.random_serial_number())
    cert = cert.not_valid_before(datetime.datetime.utcnow())
    cert = cert.not_valid_after(datetime.datetime.utcnow() + datetime.timedelta(days=100*365))
    cert = cert.add_extension(x509.BasicConstraints(ca=False, path_length=None), critical=True)
    cert = cert.add_extension(x509.KeyUsage(digital_signature=True, content_commitment=False,
                                            key_encipherment=False, data_encipherment=False,
                                            key_agreement=False, key_cert_sign=False, crl_sign=False,
                                            encipher_only=False, decipher_only=False), critical=True)
    cert = cert.add_extension(x509.SubjectKeyIdentifier.from_public_key(csr.public_key()), critical=False)
    cert = cert.add_extension(x509.AuthorityKeyIdentifier.from_issuer_public_key(ca_cert.public_key()), critical=False)
    cert = cert.sign(ca_key, hashes.SHA256(), default_backend())

    cert_pem = cert.public_bytes(serialization.Encoding.PEM).decode('utf-8')
    ca_cert_pem = ca_cert.public_bytes(serialization.Encoding.PEM).decode('utf-8')
    return cert_pem, ca_cert_pem
