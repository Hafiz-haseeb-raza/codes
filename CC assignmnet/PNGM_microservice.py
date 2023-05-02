import math as math
import psutil
import time
from flask import Flask, request, jsonify
import datetime
app = Flask(__name__)

global Primes
Primes = []

def CheckPrimes(n):
    if n < 2:
        return False
    for x in range(2, int(math.sqrt(n) + 1)):
        if (n % x) == 0:
            return False
    return True

@app.route('/generate_primes/<int:a>/<int:b>')
def generate_primes(a, b):
    for x in range(a, b+1):
        if CheckPrimes(x):
            Primes.append(x)
    return jsonify(Primes)


def monitorLess(k):
    cpu_percentages = []
    mem_percentages = []
    end_time = time.time() + k*60

    while time.time() < end_time:
        cpu_percentages.append(psutil.cpu_percent(1))
        mem_percentages.append(psutil.virtual_memory().percent)

    return cpu_percentages,mem_percentages
@app.route('/monitor/<int:k>')
def monitor(k):
    cpu_usages, mem_usages = monitorLess(k)
    data = []

    for i in range(len(cpu_usages)):
        timestamp = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        cpu = cpu_usages[i]
        mem = mem_usages[i]
        usage_data = {"timestamp": timestamp, "cpu": cpu, "memory": mem}
        data.append(usage_data)

    return jsonify(data)
@app.route('/Get')
def Get():
    return jsonify(Primes)

if __name__ == '__main__':
    app.run(debug=True)
