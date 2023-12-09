import requests
import os
from dotenv import load_dotenv
load_dotenv()


def test_generate_steps():
    """
    Tests the generate_steps endpoint.
    """
    # Get testing url
    url = os.getenv("TEST_URL")
    body = {"query": "My dishwasher is broken, what should I do?"}
    # Make request
    response = requests.post(url, json=body)
    # Check status code
    assert response.status_code == 200


def test_health():
    """
    Tests the health endpoint.
    """
    # Get testing url
    url = os.getenv("TEST_URL")
    url += "/example"
    # Make request
    response = requests.get(url)
    # Check status code
    assert response.status_code == 200


