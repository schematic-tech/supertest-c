from pathlib import Path
from conan import ConanFile
from conan.tools.files import copy


class SchematicSupertestConan(ConanFile):
    name = "schematic-supertest"
    package_type = "header-library"
    license = "MIT OR Apache-2.0"
    url = "https://github.com/schematic-tech/supertest-c"
    description = "Authoring primitives for Schematic Supertests in C"
    exports = "VERSION"
    exports_sources = "include/*", "LICENSE-MIT", "LICENSE-APACHE"
    no_copy_source = True

    def set_version(self):
        self.version = (Path(self.recipe_folder) / "VERSION").read_text().strip()

    def package(self):
        copy(self, "*.h", src=str(Path(self.source_folder) / "include"),
             dst=str(Path(self.package_folder) / "include"))
        copy(self, "LICENSE-*", src=self.source_folder,
             dst=str(Path(self.package_folder) / "licenses"))

    def package_info(self):
        self.cpp_info.bindirs = []
        self.cpp_info.libdirs = []
        self.cpp_info.set_property("cmake_file_name", "SchematicSupertest")
        self.cpp_info.set_property("cmake_target_name", "schematic::supertest")
