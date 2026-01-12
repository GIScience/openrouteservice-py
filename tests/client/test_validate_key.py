import pytest
from unittest.mock import patch

import openrouteservice
from openrouteservice.exceptions import ApiError


def test_validate_key_success():
    client = openrouteservice.Client(key="valid_key")

    with patch.object(client, "request", return_value={"ok": True}) as mock_request:
        result = client.validate_key()
        assert result is True
        mock_request.assert_called_once()


def test_validate_key_invalid_key_raises():
    client = openrouteservice.Client(key="invalid_key")

    with patch.object(client, "request", side_effect=ApiError(403, "Forbidden")):
        with pytest.raises(ApiError):
            client.validate_key()
