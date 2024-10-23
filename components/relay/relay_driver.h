#pragma once

#include <stdio.h>

#ifdef __cplusplus
extern "C" {
#endif

void relay_driver_init(int gpio_num);

void relay_driver_set_power(int gpio_num, bool power);

#ifdef __cplusplus
}
#endif

