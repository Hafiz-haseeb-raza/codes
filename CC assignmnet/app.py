import math as math
from flask import Flask, request, jsonify

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

@app.route('/is_prime/<int:n>')
def is_prime(n):
    return jsonify(CheckPrimes(n))

@app.route('/generate_primes/<int:a>/<int:b>')
def generate_primes(a, b):
    global Primes
    Primes = []
    for x in range(a, b+1):
        if CheckPrimes(x):
            Primes.append(x)
    return jsonify(Primes)

if __name__ == '__main__':
    app.run(debug=True)
