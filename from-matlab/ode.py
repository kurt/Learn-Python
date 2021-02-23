# %% Imports
from scipy.integrate import solve_ivp
from matplotlib import pyplot as plt

def exponential_decay(t, y): return -0.5 * y

sol = solve_ivp(exponential_decay, [0, 10], [2, 4, 8])

#print(sol.t)
print(sol.t.size)
print(sol.y)
print(sol.y.size)
print(sol.sol)
print(sol.y[2,1:8])

plt.title("Exponential Decay Using ODE45")
plt.xlabel("x")
plt.ylabel("y")
plt.plot(sol.t[1:8],sol.y[2,1:8],sol.t[1:8],sol.y[1,1:8],sol.t[1:8],sol.y[0,1:8])
plt.show()
