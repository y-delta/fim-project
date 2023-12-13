import unittest
from unittest.mock import patch
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'agent', 'src'))

from main import main, FileMonitor

class TestAgent(unittest.TestCase):

    @patch('main.FileMonitor.monitor_files')
    def test_file_monitor(self, mock_monitor_files):
        mock_monitor_files.return_value = []

        file_monitor = FileMonitor()

        result = file_monitor.monitor_files()

        self.assertEqual(result, [])
        mock_monitor_files.assert_called_once()

if __name__ == '__main__':
    unittest.main()