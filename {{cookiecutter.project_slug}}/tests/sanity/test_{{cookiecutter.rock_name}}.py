#
# Copyright 2024 Canonical, Ltd.
# See LICENSE file for licensing details
#

from k8s_test_harness.util import docker_util, env_util

ROCK_EXPECTED_FILES = [
    "/bin/pebble",
]


def test_{{cookiecutter.rock_name}}_rock():
    """Test {{cookiecutter.rock_name}} rock."""
    rock = env_util.get_build_meta_info_for_rock_version("{{cookiecutter.rock_name}}", "{{cookiecutter.rock_version}}", "amd64")
    image = rock.image

    # check rock filesystem.
    docker_util.ensure_image_contains_paths(image, ROCK_EXPECTED_FILES)
