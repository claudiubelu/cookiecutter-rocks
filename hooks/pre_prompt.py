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

We need to know the location of the current cookiecutter template, to use
the nested rock cookiecutter template later on.
"""

import json
import os


def store_tmp_location():
    """Store the current location on the cookiecutter template for later use."""
    with open("cookiecutter.json") as f:
        cookie_vars = json.load(f)

    cookie_vars["_template_location"] = os.getcwd()

    with open("cookiecutter.json", "w") as f:
        f.write(json.dumps(cookie_vars))


if __name__ == "__main__":
    store_tmp_location()
