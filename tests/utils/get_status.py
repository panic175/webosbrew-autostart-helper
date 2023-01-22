import unittest
from unittest.mock import patch
from homeassistant.components.webosbrew_autostart_helper.util.get_status import (
    get_status,
)
from get_status import get_status


class TestGetStatus(unittest.TestCase):
    @patch("requests.get")
    def test_get_status_success(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        result = get_status("192.168.1.100")
        mock_get.assert_called_with(
            "http://192.168.1.100:8090/json-rpc?request={%22command%22:%22serverinfo%22}",
            timeout=100,
        )
        self.assertTrue(result)
