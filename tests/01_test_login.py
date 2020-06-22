import unittest
from pages.klaudia_tester_profile_page import ProfilePage
from base import TestowanieAplikacji
from tests.helpers.screenshot import captureScreen


class LoginTest(TestowanieAplikacji):

    def test_login(self):
        pp = ProfilePage(self.driver)
        pp.move_to_profile()

        if not self.assertEqual(pp.check_ID(), 'klaudia_tester'):
            captureScreen(self, 'login_fail')


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestowanieAplikacji)
    unittest.TextTestRunner(verbosity=2).run(suite)