import unittest
from base import TestowanieAplikacji
from pages.tested_profile_page import TestedProfilePage
from pages.search_page import SearchPage
from tests.helpers.screenshot import captureScreen
import csv
from ddt import ddt, data, unpack


def get_comment_data(file_name):
    rows = []
    data_file = open(file_name, 'rt')
    reader = csv.reader(data_file)
    for row in reader:
        rows.append(row)
    return rows

@ddt
class SendMessage(TestowanieAplikacji):

    @data(*get_comment_data("message_content.csv"))
    @unpack
    def test_send_a_message(self, message_data):
        sp = SearchPage(self.driver)
        sp.move_to_search()
        sp.search_for_profile()
        tpp = TestedProfilePage(self.driver)
        tpp.send_message(message_data)

        if not self.assertEqual(tpp.check_message_content(), message_data):
            captureScreen(self, 'send_message')



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestowanieAplikacji)
    unittest.TextTestRunner(verbosity=2).run(suite)