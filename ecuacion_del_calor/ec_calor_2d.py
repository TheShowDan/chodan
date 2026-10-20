import numpy as np
import matplotlib.pyplot as plt

alpha = 111 #mm2/s
nodes = 30
L = 50 #mm
t = 3 #s
To = 20 #°C

dx = L / nodes
dy = L / nodes
dt = min(dx**2/(4*alpha), dy**2/(4*alpha))
t_nodes = int(t/dt)

#Temperatura iniciales de los nodos
T = np.zeros((nodes, nodes)) + To

#Temperatura inicial de las paredes
T[0,:] = 100
T[-1,:] = 20
T[:,0] = 100
T[:,-1] = 20


#Visualizando
fig, axis = plt.subplots()

mesh = axis.pcolormesh(T, cmap=plt.cm.jet, vmin=0, vmax=100)
plt.colorbar(mesh, ax=axis)

#Simulation
counter = 0

while counter < t:
    w = T.copy()

    for i in range(1,nodes-1):
        for j in range(1,nodes-1):

            ddTx = (w[i-1,j] - 2*w[i,j] + w[i+1,j]) / dx**2
            ddTy = (w[i,j-1] - 2*w[i,j] + w[i,j+1]) / dy**2

            T[i,j] = alpha * (ddTx + ddTy) * dt + w[i,j]

    counter += dt

    print(f't: {counter:.2f} s, Temperatura promedio: {np.average(T):.2f}°C')

    #Actualizar el grafico
    mesh.set_array(T)
    axis.set_title(f'Distribución de T a t:{counter:.2f}')

    #Mostrar el gráfico
    plt.pause(0.0001)

plt.show()
