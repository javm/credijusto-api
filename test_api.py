import requests
import pytest

def test_status_code():
    resp = requests.get('http://localhost:8000')
    assert resp.status_code == 200

def test_contains_providers():
    resp = requests.get('http://localhost:8000')
    obj = resp.json()
    rates = obj['rates']
    assert ('banxico' in rates) == True
    assert ('fixer' in rates) == True
    assert ('diario' in rates) == True
