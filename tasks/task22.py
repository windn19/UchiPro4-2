from flask import Flask

app = Flask(__name__)


def get_primes(n):
    primes = []
    number = 2
    while len(primes) < n:
        for i in range(2, number):
            if number % i == 0:
                break
        else:
            primes.append(number)
        number += 1
    return ' '.join([str(i) for i in primes])


app.add_url_rule('/primes/<int:n>', 'primes', get_primes)

if __name__ == '__main__':
    app.run(debug=True)
