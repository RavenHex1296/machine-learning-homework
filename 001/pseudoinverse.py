import numpy as np
import time

start_time = time.time()

def run():
    y = np.matrix('0; 1; 4; 9')
    data = np.matrix('1 0; 1 1; 1 2; 1 3')

    transpose = data.getT()
    data =  transpose * data
    y = transpose * y
    inverse = data.getI()
    y = inverse * y

for n in range(10):
    run()
    

print("Python:", (time.time() - start_time) / 10)