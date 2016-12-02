import logging

import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from ckan.common import config

from helpers import is_admin, is_member, is_editor

log = logging.getLogger(__name__)

class Saasportal_QuotePlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'saasportal_quote')

    def get_helpers(self):
        return {'saasportal_is_admin': is_admin,
        		'saasportal_is_member': is_member,
        		'saasportal_is_editor': is_editor}

    def get_saas_auth(self):
        saas_authorize = config.get(
            'ckanext.saas_portal_quote.saas_authorize', '')
        return {'saasportal_authorize': saas_authorize}