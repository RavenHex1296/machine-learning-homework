import time

start_time = time.time()

for num in range(10):
    total_sum = 0

    for n in range(1, 1000001):
        total_sum += n

print("Python:", (time.time() - start_time) / 10)
