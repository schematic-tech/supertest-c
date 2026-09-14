cmake_minimum_required(VERSION 3.20)
file(STRINGS "${CMAKE_CURRENT_SOURCE_DIR}/VERSION" SUPERTEST_VERSION LIMIT_COUNT 1)
project(SchematicSupertest VERSION "${SUPERTEST_VERSION}" LANGUAGES NONE)
# This header-only project has no target architecture.
set(CMAKE_INSTALL_LIBDIR "lib" CACHE PATH "Object code libraries (unused for this header-only package)")
include(GNUInstallDirs)
include(CMakePackageConfigHelpers)

add_library(schematic_supertest INTERFACE)
add_library(schematic::supertest ALIAS schematic_supertest)
set_target_properties(schematic_supertest PROPERTIES EXPORT_NAME supertest)
target_include_directories(schematic_supertest INTERFACE
    "$<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>"
    "$<INSTALL_INTERFACE:${CMAKE_INSTALL_INCLUDEDIR}>")
target_compile_features(schematic_supertest INTERFACE c_std_11)

install(TARGETS schematic_supertest EXPORT SchematicSupertestTargets)
install(FILES include/schematic.h DESTINATION "${CMAKE_INSTALL_INCLUDEDIR}")
install(FILES LICENSE-MIT LICENSE-APACHE DESTINATION "${CMAKE_INSTALL_DATADIR}/licenses/schematic-supertest")
install(EXPORT SchematicSupertestTargets NAMESPACE schematic::
    DESTINATION "${CMAKE_INSTALL_DATADIR}/cmake/SchematicSupertest")
configure_package_config_file(cmake/SchematicSupertestConfig.cmake.in
    "${CMAKE_CURRENT_BINARY_DIR}/SchematicSupertestConfig.cmake"
    INSTALL_DESTINATION "${CMAKE_INSTALL_DATADIR}/cmake/SchematicSupertest")
write_basic_package_version_file("${CMAKE_CURRENT_BINARY_DIR}/SchematicSupertestConfigVersion.cmake"
    VERSION "${PROJECT_VERSION}" COMPATIBILITY SameMajorVersion ARCH_INDEPENDENT)
install(FILES "${CMAKE_CURRENT_BINARY_DIR}/SchematicSupertestConfig.cmake"
    "${CMAKE_CURRENT_BINARY_DIR}/SchematicSupertestConfigVersion.cmake"
    DESTINATION "${CMAKE_INSTALL_DATADIR}/cmake/SchematicSupertest")

option(SUPERTEST_BUILD_TESTS "Build the authoring tests" OFF)
if(SUPERTEST_BUILD_TESTS)
    enable_language(C)
    enable_testing()
    find_package(Python3 REQUIRED COMPONENTS Interpreter)
    add_executable(authoring tests/authoring.c)
    target_link_libraries(authoring PRIVATE schematic::supertest)
    if(MSVC)
        target_compile_options(authoring PRIVATE /UNDEBUG)
    else()
        target_compile_options(authoring PRIVATE -UNDEBUG)
    endif()
    add_test(NAME authoring COMMAND "${CMAKE_COMMAND}" -E env
        "SUPERTEST_C_EXECUTABLE=$<TARGET_FILE:authoring>"
        "${Python3_EXECUTABLE}" "${CMAKE_CURRENT_SOURCE_DIR}/tests/test_authoring.py" -v)
endif()
