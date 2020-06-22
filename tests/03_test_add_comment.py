import unittest
from base import TestowanieAplikacji
from pages.tested_profile_page import TestedProfilePage
from pages.search_page import SearchPage
from tests.helpers.screenshot import captureScreen
from tests.helpers.utils import TestData


class CommentTest(TestowanieAplikacji):

    def test_add_comment(self):
        sp = SearchPage(self.driver)
        sp.move_to_search()
        sp.search_for_profile()
        tpp = TestedProfilePage(self.driver)
        tpp.pick_a_first_photo()
        tpp.add_a_comment()

        if not self.assertEqual(tpp.get_added_comment_content(), f'{TestData.login} {TestData.comment_content}'):
            captureScreen(self, 'add_a_comment_fail')


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestowanieAplikacji)
    unittest.TextTestRunner(verbosity=2).run(suite)