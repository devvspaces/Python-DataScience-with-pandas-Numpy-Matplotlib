import numpy as np
a = np.linspace(1,5,9)
b=a**2
c=a**3
d=a**4
import matplotlib.pyplot as plt
plt.plot(a,b label="Increasing Squares",color="b")
plt.plot(a,c, label="Increasing Cubes",color="r")
plt.plot(a,d, label="Increasing Quadruples", color="g")
plt.legend()
plt.xlabel("Factors")
plt.ylabel("Increments")
plt.show()