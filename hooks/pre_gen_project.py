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
We need to make sure that the number is valid.
"""

import sys


def validate_number_of_rocks(number_of_rocks):
    # We can't have < 0 rocks.
    if number_of_rocks < 1:
        print(f"ERROR: What do you mean, '{number_of_rocks}' rocks? Why are you here?")
        print("ERROR: What are you going to ask next, an imaginary number of rocks?")
        print("ERROR: Or maybe a plain ol' imaginary rock?")
        print("ERROR: GET THE ROCK OUT!")
        sys.exit(42)


if __name__ == "__main__":
    # We need this to know how many rocks to generate.
    number_of_rocks = int("{{cookiecutter.rocks}}")
    validate_number_of_rocks(number_of_rocks)
