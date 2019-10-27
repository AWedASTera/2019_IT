import matplotlib.pyplot as plt
import numpy as np

n = 40
m = 5
A = np.random.rand(n, m) * 10

def is_pareto(id, A):
    for i, vec in enumerate(A):
        if i != id and not np.any(A[id,:] > vec):
            return False
    return True

def split_by_pareto(A):
    pareto=[]
    not_pareto=[]
    for i in range(n):
        if is_pareto(i, A):
            pareto.append(A[i])
        else:
            not_pareto.append(A[i])
    return pareto, not_pareto

if __name__ == "__main__":
    vec_pareto, vec_nopareto = split_by_pareto(A)
    
    theta = 2 * np.pi * np.arange(0, 1 + 1 / m, 1 / m)
    
    fig, axes = plt.subplots(ncols=2, subplot_kw=dict(polar=True))  

    for vec in vec_pareto:
        axes[0].plot(theta, np.append(vec, vec[0]))

    for vec in vec_nopareto:
        axes[1].plot(theta, np.append(vec, vec[0]))

    plt.show()