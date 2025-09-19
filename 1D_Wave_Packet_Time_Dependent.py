#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# Parameters


L = 1
m = 1
hbar = 1
n_max = 5
x = np.linspace(0, L, 1000)


# Functions


def energy(n):
    return (n**2 * np.pi**2 * hbar**2) / (2*m*L**2)
def psi(n, x):
    return np.sqrt(2/L) * np.sin(n * np.pi * x / L)


# Plot first three stationary wavefunctions


plt.figure(figsize = (8,5))
for n in range(1, 4):
    plt.plot(x, psi(n, x))
plt.xlabel('x')
plt.ylabel(r'Wavefunction $\psi_n(x)$')
plt.title('1D Particle in a Box: First Three Stationary States')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig('C:/Users/Zohaib Hassan/Downloads/Projects/Quantum_Wave_Packets_1D_2D/plots/1D_stationary_states.png', dpi=300)
plt.show()


# Plot ground state probability density


plt.figure(figsize = (8,5))
plt.plot(x, psi(1, x)**2, color = 'blue', linestyle = ':', label=r'$|\psi_1(x)|^2$')
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.title('1D Particle in a Box: Ground State Probability Density', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.savefig('C:/Users/Zohaib Hassan/Downloads/Projects/Quantum_Wave_Packets_1D_2D/plots/1D_probability_ground.png', dpi=300)
plt.show()


# Time-dependent wavefunction (superposition of first two states)


c1, c2 = 1/np.sqrt(2), 1/np.sqrt(2)
def psi_t(x, t):
    return c1*psi(1,x)*np.exp(-1j*energy(1)*t/hbar) + c2*psi(2,x)*np.exp(-1j*energy(2)*t/hbar)


# Plot initial 1D wave packet probability density at t=0


plt.figure(figsize=(8,5))
plt.plot(x, np.abs(psi_t(x,0))**2)
plt.xlabel('x')
plt.ylabel('|Ψ(x,0)|²')
plt.title('1D Wave Packet Probability Density at t=0')
plt.grid(True, linestyle='--', alpha=0.5)
plt.savefig('C:/Users/Zohaib Hassan/Downloads/Projects/Quantum_Wave_Packets_1D_2D/plots/1D_probability_t0.png', dpi=300)
plt.show()


# Animate time evolution of the 1D wave packet


fig, ax = plt.subplots()
line, = ax.plot(x, np.abs(psi_t(x, 0))**2, label=r'$|\Psi(x,t)|^2$', color = 'red')
ax.set_ylim(0,3)
ax.set_xlabel('x')
ax.set_ylabel('|Ψ(x,t)|²')
ax.set_title('Time Evolution of 1D Wave Packet')
ax.grid(True, linestyle='--', alpha=0.5)
ax.legend()
def animate(t):
    line.set_ydata(np.abs(psi_t(x,t))**2)
    return line
anim = animation.FuncAnimation(fig, animate, frames = np.linspace(0, 20, 200), interval = 100)
anim.save('C:/Users/Zohaib Hassan/Downloads/Projects/Quantum_Wave_Packets_1D_2D/animations/1D_wavepacket.gif', writer = 'pillow', dpi=150)
plt.show()


# 2D probability density plot


Lx, Ly = 1.0, 1.0
nx, ny = 4, 4
x2 = np.linspace(0, Lx, 100)
y2 = np.linspace(0, Ly, 100)
X, Y = np.meshgrid(x2, y2)
psi2D = 2/np.sqrt((Lx*Ly))*np.sin(nx*np.pi*X/Lx)*np.sin(ny*np.pi*Y/Ly)   
plt.contourf(X, Y, psi2D**2, cmap = 'magma')
plt.colorbar(label = 'Probability Density')
plt.title(f'2D Probability Density |ψ_{nx},{ny}(x,y)|²')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True, linestyle='--', alpha=0.5)
plt.savefig(f'C:/Users/Zohaib Hassan/Downloads/Projects/Quantum_Wave_Packets_1D_2D/plots/2D_probability_{nx}_{ny}.png', dpi=300)
plt.show()


# In[ ]:




