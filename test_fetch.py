import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from paper_fetcher.fetch import fetch_papers

# Reusable mock response class
class MockResponse:
    def __init__(self, json_data=None, status_code=200):
        self._json_data = json_data or {}
        self.status_code = status_code

    def json(self):
        return self._json_data

# Test for valid paper list
def test_fetch_papers_returns_list(monkeypatch):
    mock_data = {
        "data": [
            {
                "title": "AI in Healthcare",
                "authors": [{"name": "Dr. Smith"}],
                "abstract": "Exploring AI applications.",
                "year": 2022
            }
        ]
    }

    monkeypatch.setattr("requests.get", lambda *args, **kwargs: MockResponse(mock_data, 200))
    papers = fetch_papers("AI", max_results=1)

    assert isinstance(papers, list)
    assert len(papers) == 1
    assert papers[0]["title"] == "AI in Healthcare"
    assert "Dr. Smith" in papers[0]["authors"]

# Test for empty data response
def test_fetch_papers_empty(monkeypatch):
    mock_data = {"data": []}
    monkeypatch.setattr("requests.get", lambda *args, **kwargs: MockResponse(mock_data, 200))

    papers = fetch_papers("nonexistent-topic", max_results=5)
    assert papers == []

# Test for failed API response
def test_fetch_papers_api_failure(monkeypatch):
    monkeypatch.setattr("requests.get", lambda *args, **kwargs: MockResponse(status_code=500))
    papers = fetch_papers("AI", max_results=5)
    assert papers == []
# Test for invalid response structure