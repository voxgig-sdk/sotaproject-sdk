# Sotaproject SDK feature factory

from sotaproject_sdk.feature.base_feature import SotaprojectBaseFeature
from sotaproject_sdk.feature.test_feature import SotaprojectTestFeature


def _make_feature(name):
    features = {
        "base": lambda: SotaprojectBaseFeature(),
        "test": lambda: SotaprojectTestFeature(),
    }
    factory = features.get(name)
    if factory is not None:
        return factory()
    return features["base"]()
