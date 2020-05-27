import unittest
import os
from crawling_main import *
from unittest.mock import Mock, patch

TEST_DATA_FILE = 'test_data.json'


class TestCrawling(unittest.TestCase):
  def setUp(self):
    super().setUp()
    DATA_FILE = TEST_DATA_FILE

  def tearDown(self):
    super().tearDown()
    try:
      os.remove(TEST_DATA_FILE)
    except Exception:
      pass
    
  def test_get_crawling_data(self):
    ranking_list = get_crawling_data()
    self.assertEqual(type(ranking_list), type([]))

  def test_read_write_datafile(self):
    write_dummy = {"dummy_data": "data"}
    write_json_datafile(write_dummy)
    read_dummy = read_json_datafile()
    self.assertIsNotNone(read_dummy)
    self.assertDictEqual(write_dummy, read_dummy)
  
  def test_process_crawling_data(slef):
    ranking_list = get_crawling_data()
    process_crawling_data(ranking_list)

  def test_exist_previous_data(self):
    # get ranking data
    ranking_list = get_crawling_data()
    # process data
    process_crawling_data(ranking_list)

    # get ranking data
    ranking_list = get_crawling_data()
    # process data
    process_crawling_data(ranking_list)

  def test_notify_to_server(self):
    mock_get_patcher = patch('crawling_main.requests.get')
    mock_get = mock_get_patcher.start()
    mock_get.return_value.ok = True
    mock_get.return_value.json.return_value = "aaaa".encode('utf-8')

    notify_to_server()

    mock_get_patcher.stop()
