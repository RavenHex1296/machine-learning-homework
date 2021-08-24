import time

delta = 0.1
alpha = 0.001

def f(x, y):
    return 1 + 2 * (x ** 2) + 3 * (y ** 2)

def run(x, y):
    fx = (f(1 + 0.5 * delta, 2) - f(1 - 0.5 * delta, 2)) / delta
    fy = (f(1, 2 + 0.5 * delta) - f(1, 2 - 0.5 * delta)) / delta
    x -= alpha * fx
    y -= alpha * fy

    return (x, y)

start_time = time.time()

for num in range(10):
    update_1 = run(1, 2)
    update_2 = run(update_1[0], update_1[1])

print("Python:", (time.time() - start_time) / 10)