"""Tests standard tap features using the built-in SDK tests library."""

import datetime
from unittest.mock import patch

from singer_sdk.testing import get_standard_tap_tests

from tap_mailjet.tap import Tapmailjet

SAMPLE_CONFIG = {
    "start_date": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S"),
    "api_key": "test_key",
    "api_secret": "test_secret"
}


# Run standard built-in tap tests from the SDK:
@patch('tap_mailjet.client.Client')
def test_standard_tap_tests(mocked_mailjet_client):
    """Run standard tap tests from the SDK."""
    tests = get_standard_tap_tests(
        Tapmailjet,
        config=SAMPLE_CONFIG
    )
    for test in tests:
        test()


# TODO: Create additional tests as appropriate for your tap.
