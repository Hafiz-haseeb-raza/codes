import requests

url = "http://localhost:4000/generate_primes/1/100"

response = requests.get(url)

if response.status_code == 200:
    primes = response.json()
    print(primes)
else:
    print("Error:", response.text)
