#
# Copyright 2024, Cloudbase Solutions SRL
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

"""
In some cases, we need to bundle up multiple rocks in the same repository.

We have generated the base project files, now we generate the rocks from
the rock template.

Note that cookiecutter only generates one folder, which is why the rock
template has the test files inside it.
"""

import os
import shutil
from os import path

from cookiecutter import exceptions
from cookiecutter.main import cookiecutter


def generate_rocks(template_location, number_of_rocks):
    test_dirs = ["integration", "sanity"]
    for test_dir in test_dirs:
        folder = path.join("./tests", test_dir)
        if not path.exists(folder):
            os.mkdir(folder)

    for i in range(number_of_rocks):
        # We'll try to generate a rock, and skip it if something went wrong with it.
        # It would be pretty annoying to restart the whole process just because it failed
        # for one of them.
        try:
            result_dir = cookiecutter(template_location, keep_project_on_failure=True)
        except exceptions.CookiecutterException as ex:
            print("ERROR: failed to generate rock template. Error: ", ex)
            print("Continuing with the rest of the generation.")
            continue

        # cookiecutter only generates a folder, which is why we bundled the tests there.
        # we'll have to move the tests in their proper location.
        for folder in test_dirs:
            rock_tests_dir = path.join(result_dir, "tests", folder)
            dest_tests_dir = path.join("./tests", folder)
            for file_name in os.listdir(rock_tests_dir):
                os.rename(
                    path.join(rock_tests_dir, file_name),
                    path.join(dest_tests_dir, file_name),
                )

        # Remove the tests folder.
        shutil.rmtree(path.join(result_dir, "tests"))


if __name__ == "__main__":
    template_location = "{{cookiecutter._template_location}}"
    rock_template_location = path.join(template_location, "rock_template")
    number_of_rocks = int("{{cookiecutter.rocks}}")

    generate_rocks(rock_template_location, number_of_rocks)
