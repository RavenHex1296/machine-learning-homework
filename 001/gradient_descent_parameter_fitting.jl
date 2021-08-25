function RSS(beta_0, beta_1)
    return beta_0 ^ 2 + (beta_0 + beta_1 - 1) ^ 2 + (beta_0 + 2 * beta_1 - 4) ^ 2

end

delta = 0.1
alpha = 0.001

function run(x, y)
    for n in 1:10000
        fx = (RSS(x + 0.5 * delta, y) - RSS(x - 0.5 * delta, y)) / delta
        fy = (RSS(x, y + 0.5 * delta) - RSS(x, y - 0.5 * delta)) / delta
        x -= alpha * fx
        y -= alpha * fy
    end

    return (x, y)
end

start_time = time_ns()

run(0, 2)

final_time = time_ns() - start_time

print("Julia: ", final_time/1000000000)
