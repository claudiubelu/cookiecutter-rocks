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

import json
from unittest import mock

from hooks import pre_prompt


@mock.patch("os.getcwd", autospec=True)
@mock.mock_open()
async def test_store_tmp_location(mock_open, mock_getcwd):
    mock_open.return_value = "{}"
    mock_getcwd.return_value = "/foo/lish"

    pre_prompt.store_tmp_location()

    mock_open.assert_has_calls(
        [mock.call("cookiecutter.josn"), mock.call("cookiecutter.json", "w")]
    )

    expected_dict = {"_template_location": mock_getcwd.return_value}
    mock_open.return_value.write.assert_called_once_with(json.dumps(expected_dict))
