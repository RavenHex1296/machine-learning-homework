starting_time = time_ns()


for num in 1:10
    total_sum = 0

    for n in 1:1000001
        total_sum + n 
    end
end

final_time = time_ns() - starting_time

print("Julia: ", final_time / 1000000000)
