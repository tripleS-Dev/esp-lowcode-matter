#pragma once

#include "stdbool.h"

#ifdef __cplusplus
extern "C" {
#endif

/* Definition for lp software timer */
typedef void *lp_sw_timer_handle_t;
typedef void (* lp_sw_timer_cb_t)(lp_sw_timer_handle_t, void *);

typedef struct {
    bool periodic; /* auto-reload the timer if it is periodic */
    int timeout_ms; /* timeout period */
    lp_sw_timer_cb_t handler; /* callback */
    void *arg;
} lp_sw_timer_config_t;

lp_sw_timer_handle_t lp_sw_timer_create(lp_sw_timer_config_t *config);
int lp_sw_timer_delete(lp_sw_timer_handle_t timer_handle);
int lp_sw_timer_start(lp_sw_timer_handle_t timer_handle);
int lp_sw_timer_stop(lp_sw_timer_handle_t timer_handle);
void lp_sw_timer_run(void);

#ifdef __cplusplus
}
#endif
