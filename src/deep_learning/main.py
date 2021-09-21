from typing import Union, Iterable

import numpy as np
import matplotlib.pylab as plt


# activation function
def step(x: Union[np.ndarray, Iterable, int, float]) -> np.ndarray:
    return np.array(x > 0, dtype=np.int)


if __name__ == '__main__':
    x = np.arange(-5.0, 5.0, 0.1)
    y = step(x)
    plt.plot(x, y)
    plt.ylim(-0.1, 1.1)
    plt.show()