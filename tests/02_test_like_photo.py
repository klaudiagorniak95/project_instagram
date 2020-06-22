import unittest
from base import TestowanieAplikacji
from locators import TestedPage
from pages.tested_profile_page import TestedProfilePage
from pages.search_page import SearchPage
from tests.helpers.screenshot import captureScreen


class LikeTest(TestowanieAplikacji):

    def test_give_a_like(self):
        sp = SearchPage(self.driver)
        sp.move_to_search()
        sp.search_for_profile()
        tpp = TestedProfilePage(self.driver)
        tpp.pick_a_first_photo()
        tpp.give_a_like()

        if not self.assertTrue(self.driver.find_elements_by_id(TestedPage.LIKE_BUTTON)[0].is_selected()):
            captureScreen(self, 'give_a_like_fail')

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestowanieAplikacji)
    unittest.TextTestRunner(verbosity=2).run(suite)