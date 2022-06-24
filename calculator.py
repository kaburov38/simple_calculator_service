import imp
from flask import Flask
from flask_celery import make_celery
import time
from flask import jsonify

def isPrime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = 'amqp://guest:guest@127.0.0.1:5672/'
app.config['CELERY_RESULT_BACKEND'] = 'redis://127.0.0.1:6379/0'

celery = make_celery(app)

@app.route('/api/prime/<int:n>')
def prime(n):
    temp = task_prime.delay(n)
    return jsonify(result=temp.get())

@app.route('/api/prime/palindrome/<int:n>')
def prime_palindrome(n):
    temp = task_prime_palindrome.delay(n)
    return jsonify(result=temp.get())

@celery.task(name="calculator.task_prime")
def task_prime(n):
    count = 0
    counter = 2
    while count < n:
        if isPrime(counter):
            count += 1
        counter += 1
    return counter-1

@celery.task(name="calculator.task_prime_palindrome")
def task_prime_palindrome(n):
    count = 0
    counter = 2
    while count < n:
        if isPrime(counter) and str(counter) == str(counter)[::-1]:
            count += 1
        counter += 1
    return counter-1

if __name__ == '__main__':
    app.run(debug=True)