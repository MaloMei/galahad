import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# saisir le valeurs
data = np.array([[1, 1], [2, 2], [1, 3], [3, 5], [
                4, 6], [5, 5], [5, 3], [5, 2], [6, 1]])
print(data)

# illustration des valeurs
plt.scatter(data[:, 0], data[:, 1])
plt.show()
