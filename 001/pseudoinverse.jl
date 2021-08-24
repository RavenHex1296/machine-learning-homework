starting_time = time_ns()

function run()
    y = [0; 1; 4; 9]
    data = [1 0; 1 1; 1 2; 1 3]

    transposed_matrix = transpose(data)
    data =  transposed_matrix * data
    y = transposed_matrix * y
    inverse = inv(data)
    y = inverse * y

end

for num in 1:10
    run()
end

final_time = time_ns() - starting_time
print("Julia: ", final_time / 10000000000)