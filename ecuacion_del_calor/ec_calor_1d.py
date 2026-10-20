import numpy as np
import matplotlib.pyplot as plt

#Constantes
alpha = 111 #mm2/s
nodes = 40
L = 50 #mm
t = 5 #s
To = 20 #°C

#Diferenciales
dx = L / nodes
dt = 0.5 * dx**2 / alpha
t_nodes = int(t/dt)

#Temperatura iniciales de los nodos a 20°C
T = np.zeros(nodes) + To

#Condiciones de frontera
T[0] = 100
T[-1] = 20

#Visualizando
fig, axis = plt.subplots(figsize=(10,1))

mesh = axis.pcolormesh([T], cmap=plt.cm.jet, vmin=0, vmax=100)
plt.colorbar(mesh, ax=axis, orientation='horizontal', pad=0.5)

#Simulation
counter = 0

while counter < t:
    w = T.copy()

    for i in range(1,nodes-1):
        T[i] = alpha * ((w[i-1] - 2 * w[i] + w[i+1]) / dx**2) * dt + w[i]

    counter += dt

    print(f't: {counter:.2f} s, Temperatura promedio: {np.average(T):.2f}°C')

    #Actualizar el grafico
    mesh.set_array([T])
    axis.set_title(f'Distribución de T a t:{counter:.2f}')

    #Mostrar el gráfico
    plt.pause(0.01)

plt.show()