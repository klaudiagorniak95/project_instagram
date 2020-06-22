import unittest
from pages.add_photo_page import AddPhotoPage
from pages.klaudia_tester_profile_page import ProfilePage
from time import sleep
from tests.helpers.screenshot import captureScreen
from base import TestowanieAplikacji

class AddPhotoTest(TestowanieAplikacji):

    def test_add_photo(self):
        pp = ProfilePage(self.driver)
        pp.move_to_profile()
        num_of_posts_before = pp.check_photos_quantity()
        app = AddPhotoPage(self.driver)
        app.move_to_add_photo()
        #app.allow_permission()
        app.move_to_camera()
        app.make_a_photo()
        app.add_filter()
        app.zoom_photo()
        app.add_caption()
        pp.move_to_profile()
        num_of_posts_after = pp.check_photos_quantity()

        if not self.assertEqual(num_of_posts_before + 1, num_of_posts_after):
            captureScreen(self, 'upload_photo_fail')


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestowanieAplikacji)
    unittest.TextTestRunner(verbosity=2).run(suite)