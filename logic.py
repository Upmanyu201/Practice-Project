import math

class Maths:
    def __init__(self, num):
        self.num = num

    def factorial(self):
        return math.factorial(self.num)

    def is_prime(self):
        if self.num <= 1:
            return f"No, {self.num} is not a prime number!"
        for i in range(2, int(self.num**0.5)+1):
            if self.num % i == 0:
                return f"No, {self.num} is not a prime number!"
        
        return f"{self.num} is a prime number."

    def fibonacci(self):
        if self.num <= 0:
            return []
        elif self.num <= 1:
            return [0]
        else:
            series = [0,1]
            while len(series) < self.num:
                next_term  = series[-1] + series[-2]
                series.append(next_term)
            return series

