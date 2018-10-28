from lib.ui.login_page import LoginPage
from lib.utils import create_driver
import unittest
class TestSample(unittest.TestCase):
    def setUp(self):
        self.driver = create_driver.get_driver_instance()
        self.login = LoginPage(self.driver)
    def tearDown(self):
        self.driver.close()
    def test_Sample(self):
        self.login.wait_for_login_page_to_load()
        actual_title =self.driver.title
        expected_title = 'actiTime - Login'
        assert actual_title == expected_title
