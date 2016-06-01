using Gadfly
using Distributions

M = 3
a = [0.5,-0.02,-0.4]
N = 1000

d = Normal(0,1)
srand(1)

x = zeros(N)
for i in 1:M
	x[i] = rand(d,1)[1]
end

for i in M+1:N
	for j in 1:M
    x[i] += a[j]*x[i-j]
  end
  x[i] += rand(d,1)[1]
end

t = 1:N
plot(x=t,y=x,Geom.line)

function c(k)
  ans = 0
  for i in 1:N-k
    ans += x[i] * x[i+k]
  end
  return ans / N
end

C_m = zeros(M,M)
for i in 1:M
  for j in 1:M
    C_m[i,j] = c(abs(j-i))
  end
end

c_m = zeros(M)
for i in 1:M
	c_m[i] = c(i)
end

a_m = (C_m)\(c_m)
sigma = c(0) - (c_m)' * a_m
println(a)
println(a_m)
println(sigma)
