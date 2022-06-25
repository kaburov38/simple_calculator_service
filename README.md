# simple_calculator_service
## description
In this simple calculator service I use flask and celery to make an asynchronous service. I use rabbitmq for the celery broker and redis for the backend. This service has 2 functions which are prime and prime_palindrome. prime function will return nth prime number and prime palindrome will return nth prime palindrome number.