import matplotlib.pyplot as plt

fig, ax = plt.subplots()
t = [-3, 1, 2, -2, 3, -1]
ax.plot(t)
ax.set_xlabel('x axis')
ax.set_ylabel('y axis')

example_a = [2 - i for i in t]
ax.plot(example_a)

example_b = [(i / 3) * 2 + 1 for i in t]
ax.plot(example_b)

example_c = [i*i for i in t]
ax.plot(example_c)

example_d = [2**i for i in t]
ax.plot(example_d)

example_e = [(2**i) - (i**3) for i in t]
ax.plot(example_e)

plt.show()