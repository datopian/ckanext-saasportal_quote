import logging

import ckan.plugins.toolkit as toolkit

log = logging.getLogger(__name__)


def is_user_in_org(context=None):
    organizations = toolkit.get_action('organization_list_for_user')(context = context, data_dict={'permission': 'read'})
    if len(organizations) != 0:
        return True
    return False