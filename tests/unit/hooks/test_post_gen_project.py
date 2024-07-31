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

import itertools
from os import path
from unittest import mock

from cookiecutter import exceptions

from hooks import post_gen_project


@mock.patch.object(post_gen_project, "cookiecutter", autospec=True)
@mock.patch("shutil.rmtree", autospec=True)
@mock.patch("os.rename", autospec=True)
@mock.patch("os.listdir", autospec=True)
@mock.patch("os.mkdir", autospec=True)
@mock.patch("os.path.exists", autospec=True)
def test_generate_rocks(
    mock_exists, mock_mkdir, mock_listdir, mock_rename, mock_rmtree, mock_cookiecutter
):
    # A folder is created only if it's missing.
    mock_exists.side_effect = [True, False]

    # Generate an exception for the second rock.
    rock_result1 = "/bar/tender"
    rock_result2 = exceptions.CookiecutterException("The cookie has crumbled")
    rock_result3 = "/ora/ora/ora"
    mock_cookiecutter.side_effect = [rock_result1, rock_result2, rock_result3]

    fake_file = "test_rocky.py"
    mock_listdir.return_value = [fake_file]

    fake_location = "/foo/lish"

    post_gen_project.generate_rocks(fake_location, 3)

    mock_mkdir.assert_called_once_with(path.join("./tests", "sanity"))
    mock_cookiecutter.assert_has_calls(
        [mock.call(fake_location, keep_project_on_failure=True)] * 3
    )

    # we have 4 calls for os.rename.
    pairs = itertools.product([rock_result1, rock_result3], ["integration", "sanity"])
    calls = [
        mock.call(
            path.join(x, "tests", y, fake_file), path.join("./tests", y, fake_file)
        )
        for (x, y) in pairs
    ]
    mock_rename.assert_has_calls(calls)

    mock_rmtree.assert_has_calls(
        [
            mock.call(path.join(rock_result1, "tests")),
            mock.call(path.join(rock_result3, "tests")),
        ]
    )
