import pytest
import requests

@pytest.mark.parametrize("url", [
    "https://www.bankier.pl/new-charts/get-data?symbol=EURPLN&intraday=false&type=area&max_period=true",
    "https://www.bankier.pl/new-charts/get-data?symbol=USDPLN&intraday=false&type=area&max_period=true",
    "https://www.bankier.pl/new-charts/get-data?symbol=GBPPLN&intraday=false&type=area&max_period=true"   
])
def test_data_retrieval(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200

    # Assert that the response contains data
    assert response.json() is not None