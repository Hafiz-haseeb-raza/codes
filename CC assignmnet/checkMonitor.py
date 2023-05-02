import time
import requests

def test_monitor(k):
    # Call the monitor endpoint
    response = requests.get(f"http://127.0.0.1:5000/monitor/{k}")
    data = response.json()

    # Print the CPU and memory usage for the last k minutes
    print(f"CPU usage for last {k} minutes: {data['cpu_usages']}")
    print(f"Memory usage for last {k} minutes: {data['mem_usages']}")

if __name__ == "__main__":
    # Test with k = 1 minute
    test_monitor(1)
    time.sleep(30)
    test_monitor(1)
    time.sleep(30)
    test_monitor(1)