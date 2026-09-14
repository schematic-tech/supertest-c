# This overlay consumes the checkout containing it. Release overlays download a
# versioned source asset and verify its SHA512 instead (scripts/release.py).
get_filename_component(SOURCE_PATH "${CMAKE_CURRENT_LIST_DIR}/../.." ABSOLUTE)
vcpkg_cmake_configure(SOURCE_PATH "${SOURCE_PATH}" OPTIONS -DSUPERTEST_BUILD_TESTS=OFF)
vcpkg_cmake_install()
vcpkg_cmake_config_fixup(PACKAGE_NAME SchematicSupertest CONFIG_PATH share/cmake/SchematicSupertest)
file(REMOVE_RECURSE "${CURRENT_PACKAGES_DIR}/debug")
vcpkg_install_copyright(FILE_LIST "${SOURCE_PATH}/LICENSE-MIT" "${SOURCE_PATH}/LICENSE-APACHE")
file(INSTALL "${CMAKE_CURRENT_LIST_DIR}/usage" DESTINATION "${CURRENT_PACKAGES_DIR}/share/${PORT}")
