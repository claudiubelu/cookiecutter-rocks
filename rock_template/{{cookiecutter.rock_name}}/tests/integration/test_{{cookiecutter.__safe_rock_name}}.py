#
# Copyright 2024 Canonical, Ltd.
# See LICENSE file for licensing details
#

import logging

from k8s_test_harness import harness
from k8s_test_harness.util import env_util

LOG = logging.getLogger(__name__)


def test_integration_{{cookiecutter.__safe_rock_name}}(function_instance: harness.Instance):
    rock = env_util.get_build_meta_info_for_rock_version("{{cookiecutter.rock_name}}", "{{cookiecutter.rock_version}}", "amd64")

    LOG.info(f"Using rock: {rock.image}")
    LOG.warn("Integration tests are not yet implemented yet")
