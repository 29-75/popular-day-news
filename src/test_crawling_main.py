import unittest
import crawling_main
import os

TEST_DATA_FILE = 'test_data.json'


class TestCrawling(unittest.TestCase):
	def setUp(self):
	 return super().setUp()

	def test_get_popular_day_ranking(self):
		ranking_list = crawling_main.get_popular_day_ranking()

		self.assertEqual(type(ranking_list), type([]))

	def test_read_write_datafile(self):
		crawling_main.DATA_FILE = TEST_DATA_FILE

		write_dummy = {"dummy_data": "data"}
		crawling_main.write_json_datafile(write_dummy)
		read_dummy = crawling_main.read_json_datafile()

		self.assertIsNotNone(read_dummy)
		self.assertDictEqual(write_dummy, read_dummy)
		os.remove(TEST_DATA_FILE)

	def test_not_exist_previous_data(self):
		crawling_main.DATA_FILE = TEST_DATA_FILE
		crawling_main.main()

	def test_normal_state_main(self):
		crawling_main.DATA_FILE = TEST_DATA_FILE
		crawling_main.main()
		os.remove(TEST_DATA_FILE)

	def test_notify_to_server(self):
		crawling_main.notify_to_server()
