import numpy as np


def Rx(theta):
    return np.array(
        [
            [1, 0, 0],
            [0, np.cos(theta), -np.sin(theta)],
            [0, np.sin(theta), np.cos(theta)],
        ]
    )


def Ry(theta):
    return np.array(
        [
            [np.cos(theta), 0, np.sin(theta)],
            [0, 1, 0],
            [-np.sin(theta), 0, np.cos(theta)],
        ]
    )


def Rz(theta):
    return np.array(
        [
            [np.cos(theta), -np.sin(theta), 0],
            [np.sin(theta), np.cos(theta), 0],
            [0, 0, 1],
        ]
    )


def Rotation(axe, theta):
    if axe == "x":
        return Rx(theta)
    elif axe == "y":
        return Ry(theta)
    elif axe == "z":
        return Rz(theta)
    elif axe == "id":
        return np.identity(3)


def position_bras(thetas, axes, vectors,P0):
    P_liste = []
    M_liste = []

    M0 = np.identity(3)

    P_liste.append(P0)
    M_liste.append(M0)

    for n in range(0, len(vectors)):
        P_n = P_liste[n]
        M_n = M_liste[n]

        P_np1 = P_n + (M_n @ vectors[n])
        P_liste.append(P_np1)

        if n+1 < len(axes):
            M_np1 = M_n @ Rotation(axes[n+1], thetas[n+1])
            M_liste.append(M_np1)

    return P_liste