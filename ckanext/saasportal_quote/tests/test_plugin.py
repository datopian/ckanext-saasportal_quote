from ckan.tests import helpers
import unittest
from ckan import plugins
from ckanext.saasportal_quote.plugin import get_saas_auth


class ActionBase(unittest.TestCase):
    @classmethod
    def setup_class(self):
        if not plugins.plugin_loaded('saasportal_quote'):
            plugins.load('saasportal_quote')
        helpers.reset_db()

    def setup(self):
        helpers.reset_db()

    @classmethod
    def teardown_class(self):
        if plugins.plugin_loaded('saasportal_quote'):
            plugins.unload('saasportal_quote')


class TestPlugin(ActionBase):
    @helpers.change_config('ckanext.saasportal_quote.saas_authorize', 'MyTest')
    def test_get_saas_auth(self):
        saas_authorize = get_saas_auth()
        if saas_authorize == 'MyTest':
            assert True
        else:
            assert False
