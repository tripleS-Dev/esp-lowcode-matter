idf_component_register(SRC_DIRS led utils .
                       INCLUDE_DIRS led utils .
                       REQUIRES lp_sw_timer)

target_include_directories(
    ${COMPONENT_LIB} PRIVATE ${COMPONENT_INCLUDES}
)
