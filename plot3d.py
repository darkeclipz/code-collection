import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from numpy import *
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d
from sympy import symbols, diff, solve, Matrix
from matplotlib import cm as cm
font = {'size': 14}
plt.rc('font', **font)

class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0,0), (0,0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
        FancyArrowPatch.draw(self, renderer)

def plot3d(f,lim=(-5,5),title='Surface plot',detail=0.05,path=[],points=[]):
    fig = plt.figure(figsize=(16,12))
    ax = fig.add_subplot(111, projection='3d')
    xs = ys = np.arange(lim[0],lim[1], detail)
    X, Y = np.meshgrid(xs, ys)
    zs = np.array([f(x, y) for x, y in zip(np.ravel(X), np.ravel(Y))])
    Z = zs.reshape(X.shape)
    surf = ax.plot_surface(X, Y, Z, cmap=cm.Blues)
    fig.colorbar(surf, shrink=0.5, aspect=5)
    ax.set_xlabel('X-axis');ax.set_ylabel('Y-axis');ax.set_zlabel('Z-axis')
    plt.title(title)
    if len(path):
        xs, ys, zs = path[0], path[1], path[2]
        ax.plot(xs,ys,zs, 'o', color='r', markersize=5, zorder=3)
        for i in range(len(xs)-1):
            ax.add_artist(Arrow3D([xs[i], xs[(i+1)%len(xs)]], 
                                  [ys[i], ys[(i+1)%len(xs)]], 
                                  [zs[i], zs[(i+1)%len(xs)]],
                                  mutation_scale=15, lw=2, arrowstyle="-|>", 
                                  color='r', zorder=4)) 
    if len(points):
        ax.plot(points[0], points[1], [f(x,y) for x, y in zip(points[0], points[1])], 'o', 
            color='r', markersize=5, zorder=3)
    plt.show()