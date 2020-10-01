"""
Helpers for the credentials service.
"""

from django.conf import settings

from openedx.core.djangoapps.site_configuration import helpers as config_helpers


def is_learner_records_enabled():
    return config_helpers.get_value(
        "ENABLE_LEARNER_RECORDS", settings.FEATURES["ENABLE_LEARNER_RECORDS"]
    )


def is_learner_records_enabled_for_org(org):
    return config_helpers.get_value_for_org(
        org, "ENABLE_LEARNER_RECORDS", settings.FEATURES["ENABLE_LEARNER_RECORDS"]
    )
