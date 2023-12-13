import math

def calc_sinh(x):
    result = (math.e**(x) - math.e**(-x)) / 2
    return result

print(calc_sinh(0))  # 0.0
print(calc_sinh(1))  # 1.1752011936438014
