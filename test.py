import math

def f(x):
    return 

def dRSS_da(points, a, b):
    total = 0

    for point in points:
        total += 2 * (a * point[0] ** b - point[1]) * (point[0] ** b)

    return total

def dRSS_db(points, a, b):
    total = 0

    for point in points:
        total += 2 * (a * point[0] ** b - point[1]) * (math.log(point[0]) * point[0] ** b)

    return total

def rss(funct, points):
    rss = 0

    for point in points:
        x, y = point
        prediction = funct(x)
        rss += (y - prediction) ** 2

    return rss

def run(points, dRSS_da, dRSS_db, a, b, alpha, num_steps):
    print("Initial RSS:", rss(lambda x: a * x ** b, points))

    for _ in range(num_steps):
        a = a - dRSS_da(points, a, b) * alpha
        b = b - dRSS_db(points, a, b) * alpha

    print('Final RSS:', rss(lambda x: a*x**b, points))

    return (a, b)

actual_points = [(1, 1), (2, 2), (3, 9), (4, 16)]

'''
print(run(actual_points, dRSS_da, dRSS_db, 0.80, 2.065, 0.00001, 1))

def f(x):
    return 0.8 * x ** 2.06528585854

'''