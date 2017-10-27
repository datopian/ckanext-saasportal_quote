import logging

import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from pylons import config

log = logging.getLogger(__name__)


def get_saas_auth():
    saas_authorize = config.get(
        'ckanext.saasportal_quote.saas_authorize', '')
    return saas_authorize


class Saasportal_QuotePlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'saasportal_quote')

    def get_helpers(self):
        return {'saasportal_authorize': get_saas_auth}
