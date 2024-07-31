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

from unittest import mock

from rock_template.hooks import pre_gen_project


@mock.patch("sys.exit", autospec=True)
def test_verify_values(mock_exit):
    for valid_name in ["foo", "foo_lish", "foo-lish", "f00-l1sh"]:
        pre_gen_project.verify_rock_name(valid_name)
        mock_exit.assert_not_called()

    for invalid_name in ["f", "0foo", "-foo", "foo lish", " foo"]:
        mock_exit.reset_mock()

        pre_gen_project.verify_rock_name(invalid_name)
        mock_exit.assert_called_once_with(42)
