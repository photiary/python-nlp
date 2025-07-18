# test_api.py
import requests
import json

def test_api():
    base_url = "http://localhost:8001"
    
    # Test root endpoint
    print("Testing root endpoint...")
    response = requests.get(f"{base_url}/")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    print()
    
    # Test raw news endpoint
    print("Testing raw news endpoint...")
    response = requests.get(f"{base_url}/api/raw-news/1")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    print()
    
    # Test filter endpoint
    print("Testing filter endpoint...")
    response = requests.post(f"{base_url}/api/filter/1")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")

if __name__ == "__main__":
    test_api() 