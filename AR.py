import numpy as np

M = 3
a = np.array([0.5,-0.02,-0.4])
N = 1000

np.random.seed(1)
x = np.zeros(N)
for i in range(M):
    x[i] = np.random.normal(0,1)

for i in range(M,N):
    for j in range(M):
        x[i] += a[j] * x[i-j-1]
    x[i] += np.random.normal(0,1)

def c(k):
    ans = 0
    for i in range(N-k):
        ans += x[i] * x[i+k]
    return ans / N

C_m = np.zeros((M,M))
for i in range(M):
    for j in range(M):
        C_m[i][j] = c(abs(j-i))

c_m = np.zeros(M)
for i in range(M):
    c_m[i] = c(i+1)

# a_m = np.dot(np.linalg.inv(C_m),c_m)
a_m = np.linalg.solve(C_m,c_m)
sigma = c(0) - np.dot(c_m.T,(a_m))

print("a =",a)
print("a_m=",a_m)
print("sigma=",sigma)
