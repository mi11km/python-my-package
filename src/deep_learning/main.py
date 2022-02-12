import numpy as np


def step(x):
    return np.array(x > 0, dtype=int)

def update_weight_parameters(weight, data, learning_rate):
    if step(np.dot(data[0], weight)) == data[1]:
        print("重み更新なし")
        return weight
    if data[1] == 0:
        print("偽陽性")
        return weight-data[0]*learning_rate
    if data[1] == 1:
        print("偽陰性")
        return weight+data[0]*learning_rate

if __name__ == '__main__':
    a = 0.5
    w0 = np.array([-2, 2, 2])

    p1 = (np.array([1, 0, 2]), 0)
    p2 = (np.array([1, 3, 4]), 1)
    p3 = (np.array([1, -1, -2]), 0)
    p4 = (np.array([1, 1, 0]), 1)

    w1 = update_weight_parameters(w0, p1, a)
    print(w1)

    w2 = update_weight_parameters(w1, p2, a)
    w3 = update_weight_parameters(w2, p3, a)
    w4 = update_weight_parameters(w3, p4, a)

    print(w4)