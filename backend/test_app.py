import requests
import os
from dotenv import load_dotenv
load_dotenv()


def test_health():
    """
    Tests the health endpoint.
    """
    # Get testing url
    url = "http://iproject4-flask.azurewebsites.net"
    url += "/example"
    # Make request
    response = requests.get(url)
    # Check status code
    assert response.status_code == 200


