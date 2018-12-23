import matplotlib.pyplot as plt
from sklearn.datasets import make_moons

Xtoy, ytoy = make_moons(n_samples=100, random_state=123)

plt.scatter(Xtoy[ytoy == 0, 0], Xtoy[ytoy == 0, 1], color='red', marker='^', alpha=0.5)
plt.scatter(Xtoy[ytoy == 1, 0], Xtoy[ytoy == 1, 1], color='blue', marker='o', alpha=0.5)

plt.tight_layout()
# plt.savefig('./figures/half_moon_1.png', dpi=300)
plt.show()