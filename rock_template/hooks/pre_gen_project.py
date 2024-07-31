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

import re
import sys

VALID_ROCK_REGEX = r"^[_a-zA-Z][-_a-zA-Z0-9]+$"


def verify_rock_name(rock_name):
    if not re.match(VALID_ROCK_REGEX, rock_name):
        print(f"ERROR: {rock_name} is not a valid rock name!")
        sys.exit(42)


if __name__ == "__main__":
    rock_name = "{{cookiecutter.rock_name}}"
    verify_rock_name(rock_name)
