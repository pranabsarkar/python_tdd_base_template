import json
from unittest import TestCase
from unittest.mock import patch
from src.sample_interface import SampleInterface

with open('./tests/fixtures/sample_interface.json') as f:
    resp = json.load(f)


class TestSampleInterface(TestCase):
    def setUp(self) -> None:
        self.client = SampleInterface()

    @patch('src.sample_interface.SampleInterface.sample_module')
    def test_sample_module(self, mock_sample):
        mock_sample.return_value = resp
        result = self.client.sample_module()
        self.assertIsNotNone(result)
        self.assertIsInstance(result, dict)
        self.assertEqual(resp, result)
