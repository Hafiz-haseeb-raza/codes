import concurrent.futures
import requests

def test_generate_primes():
    inputs = [(1, 20000000), (10, 20), (20, 30)]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_to_input = {executor.submit(requests.get, f'http://127.0.0.1:5000/generate_primes/{a}/{b}'): (a, b) for a, b in inputs}

        for future in concurrent.futures.as_completed(future_to_input):
            a, b = future_to_input[future]
            result = future.result().json()
            print(f"Primes between {a} and {b}: {result}")

if __name__ == '__main__':
    test_generate_primes()
