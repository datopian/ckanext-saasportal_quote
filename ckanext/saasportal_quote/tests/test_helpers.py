from ckan.tests import helpers, factories
import unittest
from ckan import plugins, logic
from ckanext.saasportal_quote import helpers as h


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


class TestHelpers(ActionBase):
    def test_is_user_in_org(self):
        user = factories.User()
        test_org = factories.Organization(
            users=[
                {'name': user['name'], 'capacity': 'admin'}
            ]
        )
        context = {
            'user': user['name']
        }

        self.assertTrue(h.is_user_in_org(context=context))

    def test_user_is_not_in_org(self):
        u = factories.User()
        context = {
            'user': u['name']
        }
        self.assertFalse(h.is_user_in_org(context=context))
