#x = [1 0; 1 log(2); 1 log(3); 1 log(4)]
#xt = transpose(x)
#y = [0; log(2); log(9); log(16)]
#n = inv(xt*x)
#println(exp(-0.2247750071111776))
#println(2.0648047071821365)
function run(x, y)
    xt = transpose(x)
    n = inv(xt*x)
    return n*(xt*y)

end
x = [1 1; 1 3; 1 5]
y = [4; 16; 25]

println(run(x, y))
