idf_component_register(
    SRCS "src/display_ssd1306.c" "src/display_ssd1306_fonts.c"
    INCLUDE_DIRS "include"
    REQUIRES i2c
)
