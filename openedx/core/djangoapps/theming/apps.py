
from __future__ import absolute_import

from django.apps import AppConfig

from openedx.core.djangoapps.plugins.constants import PluginURLs, ProjectType

plugin_urls_config = {PluginURLs.NAMESPACE: u'theming', PluginURLs.REGEX: r'^theming/'}


class ThemingConfig(AppConfig):
    name = 'openedx.core.djangoapps.theming'
    plugin_app = {
        PluginURLs.CONFIG: {
            ProjectType.CMS: plugin_urls_config,
            ProjectType.LMS: plugin_urls_config,
        }
    }
    verbose_name = "Theming"

    def ready(self):
        # settings validations related to theming.
        from . import checks
