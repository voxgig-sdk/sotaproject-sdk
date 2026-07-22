# ProjectName SDK exists test

import pytest
from sotaproject_sdk import SotaprojectSDK


class TestExists:

    def test_should_create_test_sdk(self):
        testsdk = SotaprojectSDK.test(None, None)
        assert testsdk is not None
