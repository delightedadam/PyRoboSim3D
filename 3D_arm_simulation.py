import numpy as np
import matplotlib.pyplot as plt

#The order of the cells corresponds to that of the vectors 


#don't touch this ----
def Rx(theta):
    return np.array([[1, 0, 0],
                    [0, np.cos(theta), -np.sin(theta)],
                    [0, np.sin(theta),  np.cos(theta)]])   


def Ry(theta):
    return np.array([[np.cos(theta), 0, np.sin(theta)],
                     [0,             1, 0            ],
                     [-np.sin(theta), 0, np.cos(theta)]])

def Rz(theta):
    return np.array([[np.cos(theta), -np.sin(theta), 0],
                     [np.sin(theta),  np.cos(theta), 0],
                     [0,              0,             1]])

def Rotation(axe, theta):
    if axe == 'x':
        return Rx(theta)
    elif axe == 'y':
        return Ry(theta)
    elif axe == 'z':
        return Rz(theta)

def P_n(n, A, V, theta):
    assert(n<len(A))
    M = Rotation(A[0], theta[0]) 
    U = V[0]
    if n == 0: return U, M
    for i in range(1, n+1):
        U = U + (M @ V[i])
        M = M @ Rotation(A[i], theta[i])
    return U, M

#here you have to choose if yu want a 360 rotation or a vertical rotation on y or x axe 
A = ['z', 'y', 'y', 'y', 'y','y','z'] #those letters are examples you can remove it to put yours 


#here you have to put yure vectors coord ([x,y,z]) , the numbers are just examples you can remove it 
V = [
    np.array([0, 0,10 ]),   # V0
    np.array([0,10,11]),    # V1
    np.array([0, 0, 22]),   # V2
    np.array([0, 0, 27]),   # V3
    np.array([0,  10, 7]),  # V4
    np.array([0,10,9]),     #V5s
    np.array([0,14,0])      #V6
    ]

#here you have to put the angles  , again it's just an example you can remove it 
angles = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
articulation_active = 0

#here you have to put the colors of every vector again , again it's just an example you can remove it 
couleurs = ['black', 'blue', 'orange', 'green', 'purple','black', 'blue', 'orange', 'green']

TAILLE_FLECHES = 1.0    

def dessiner_robot():
    ax.clear()
    avant = np.array([0, 0, 0])
    
    for i in range(len(V)):
        actuel, _ = P_n(i, A, V, angles)
        fleche = actuel - avant
        
        epaisseur = 5 if i == articulation_active else 2
        
        ax.quiver(avant[0], avant[1], avant[2], fleche[0], fleche[1], fleche[2],
                  color=couleurs[i], arrow_length_ratio=0.12, linewidth=epaisseur,
                  length=TAILLE_FLECHES)
        
        avant = actuel
    ax.set_xlim([-40, 160])
    ax.set_ylim([-40, 160])
    ax.set_zlim([0, 160])
    
    ax.set_xlabel('X (cm)')
    ax.set_ylabel('Y (cm)')
    ax.set_zlabel('Z (cm)')
    ax.set_title(f"test")
    fig.canvas.draw_idle()

def on_key(event):
    global articulation_active
    
    if event.key == 'right':
        articulation_active = (articulation_active + 1) % len(V)
    elif event.key == 'left':
        articulation_active = (articulation_active - 1) % len(V)
    elif event.key == 'up':
        angles[articulation_active] += 0.1
    elif event.key == 'down':
        angles[articulation_active] -= 0.1

    dessiner_robot()

fig = plt.figure(figsize=(9, 7))
ax = fig.add_subplot(111, projection='3d')
fig.canvas.mpl_connect('key_press_event', on_key)

dessiner_robot()
plt.show()