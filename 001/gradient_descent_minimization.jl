function f(x, y)
    return 1 + 2 * (x * x) + 3 * (y * y)
end

delta = 0.1
alpha = 0.001

function run(x, y)
    fx = (f(x + 0.5 * delta, y) - f(x - 0.5 * delta, y)) / delta
    fy = (f(x, y + 0.5 * delta) - f(x, y - 0.5 * delta)) / delta
    x -= alpha * fx
    y -= alpha * fy

    return (x, y)

end

start_time = time_ns()

for n in 1:10
    update_1 = run(1,2)
    update_2 = run(update_1[1], update_1[2])

end

final_time = time_ns() - start_time

print("Julia: ", final_time/10000000000)
