import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

def punto1():
    #% matplotlib inline --> El codigo fue ejecutado en Pycharm, por ende, no fue necesario el uso de este comando.
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    x, y, z = np.meshgrid(np.linspace(0, 2, 10),  # Rango de valores en el eje x divide el intervalo [-2,2] en 10 partes
                          np.linspace(0, 2, 10),  # Rango de valores en el eje y divide el intervalo [-2,2] en 10 partes
                          np.linspace(0, 2, 10))  # Rango de valores en el eje z divide el intervalo [-2,2] en 10 partes
    u = y*z*np.exp(x*z)  # Primera componente del campo vectorial
    v = np.exp(x*z)  # Segunda componente del campo vectorial
    w = x*y*np.exp(x*z)  # Tercera componente del campo vectorial
    t = np.linspace(0, 1)
    x_1 = np.sqrt(t)
    y_1 = t + 1
    z_1 = t ** 2
    plt.plot(x_1, y_1, z_1)
    ax.quiver(x, y, z, u, v, w, length=0.005, color='green')  # Genera el campo vectorial en en espacio
    plt.show()  # Grafica el campo vectorial
def punto2():
    #% matplotlib inline --> El codigo fue ejecutado en Pycharm, por ende, no fue necesario el uso de este comando.
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    x, y, z = np.meshgrid(np.linspace(0, 3, 10),  # Rango de valores en el eje x divide el intervalo [-2,2] en 10 partes
                          np.linspace(0, 3, 10),  # Rango de valores en el eje y divide el intervalo [-2,2] en 10 partes
                          np.linspace(0, 3, 10))  # Rango de valores en el eje z divide el intervalo [-2,2] en 10 partes
    u = x * y # Primera componente del campo vectorial
    v = 4 * (x**2)  # Segunda componente del campo vectorial
    w = y*z # Tercera componente del campo vectorial

    X= np.linspace(0,1,10)
    Y= np.linspace(0,1,10)
    X,Y = np.meshgrid(X,Y)
    Z = X*np.exp(Y)
    ax.plot_surface(X,Y,Z) #Grafica la superficie 

    ax.quiver(x, y, z, u, v, w, length=0.005, color='green')  # Genera el campo vectorial en en espacio

    plt.show()  # Grafica el campo vectorial
if __name__ == '__main__':
    #punto1()
    punto2()
