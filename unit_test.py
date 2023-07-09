import pytest
from flask import Flask, jsonify
import chatbot

# create a pytest fixture for the flask test client
@pytest.fixture
def client():
    chatbot.app.config['TESTING'] = True

    with chatbot.app.test_client() as client:
        yield client

# test the /get_response endpoint
def test_get_response(client):
    # send a post request with a sample message
    response = client.post('/get_response', json={'message': 'hello'})

    # check the response status code
    assert response.status_code == 200

    # check the response data
    data = response.get_json()
    assert 'message' in data
    assert isinstance(data['message'], str)
