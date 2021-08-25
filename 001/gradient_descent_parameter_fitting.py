import time

alpha = 0.001
delta = 0.1

def RSS(beta_0, beta_1):
    return beta_0 ** 2 + (beta_0 + beta_1 - 1) ** 2 + (beta_0 + 2 * beta_1 - 4) ** 2

def run(x, y):
    fx = (RSS(x + 0.5 * delta, y) - RSS(x - 0.5 * delta, y)) / delta
    fy = (RSS(x, y + 0.5 * delta) - RSS(x, y - 0.5 * delta)) / delta
    x -= alpha * fx
    y -= alpha * fy

    return (x, y)

start_time = time.time()

x = 0
y = 2

for n in range(1, 10001):
  update = run(x, y)
  x = update[0]
  y = update[1]

print("Python:", (time.time() - start_time))