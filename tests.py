import math


def dRSS_da(a, b):
    return 2 * b * (a * b - 2) + 2 * (b ** 2) * (a * (b ** 2) - 8) +  2 * (b ** 2.25) * (a * (b ** 2.25) - 16) +  2 * (b ** 2.5) * (a * (b ** 2.5) - 25)


def dRSS_db(a, b):
    return 2*a*(a*b-2) + 4*a*b*(a*(b**2)-8) + 4.5*a*(b**1.25)*(a*(b**2.25)-16) + 5*a*(b**1.5)*(a*(b**2.5)-25)

def rss(funct, points):
    rss = 0

    for point in points:
        x, y = point
        prediction = funct(x)
        rss += (y - prediction) ** 2

    return rss

def run(points, dRSS_da, dRSS_db, a, b, alpha, num_steps):
    print(rss(lambda x: a * b ** x, points))

    for _ in range(num_steps):
        a = a - dRSS_da(a, b) * alpha
        b = b - dRSS_db(a, b) * alpha

    print(rss(lambda x: a * b ** x, points))

    return (a, b)

actual_points = [(1, 2), (2, 8), (2.25, 16), (2.5, 25)]

print(run(actual_points, dRSS_da, dRSS_db, 1.0817, 1.9402, 0.00001, 100000))

def f(x):
    return 2 * (3 ** x)

print(rss(f, actual_points))