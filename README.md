README

# Quantum Wave Packets in 1D and 2D

## Overview
This project demonstrates **quantum wave packet simulations** in both **1D and 2D infinite potential wells** using Python.  
It includes **stationary wavefunctions**, **probability densities**, and **time-dependent animations** of 1D wave packets, as well as **2D probability density plots**.  

This project is designed to showcase **computational physics skills** for CVs and GitHub portfolios.

---

## Features

### 1D Simulations
- **Stationary Wavefunctions:** First three eigenstates ψ₁(x), ψ₂(x), ψ₃(x)  
- **Probability Density:** Ground state probability |ψ₁(x)|²  
- **Time-Dependent Wave Packet:** Superposition of first two states with animation showing |Ψ(x,t)|² over time  

**Files generated:**  
- `plots/1D_stationary_states.png` → First three stationary states  
- `plots/1D_probability_ground.png` → Ground state probability density  
- `plots/1D_probability_t0.png` → Initial wave packet probability density  
- `animations/1D_wave_packet.gif` → Time evolution animation  

### 2D Simulations
- **Single 2D Stationary State:** |ψ₄₄(x,y)|²  
- **Time-Dependent Wave Packet:** Superposition of two 2D states (nx1,ny1) = (1,1) and (nx2,ny2) = (2,1) showing |Ψ(x,y,t)|² over time  

**Files generated:**  
- `plots/2D_probability_4_4.png` → Single 2D stationary state  
- `plots/2D_wave_packet.png` → Initial 2D wave packet probability density  
- `animations/2D_wave_packet.gif` → Time evolution animation 

---

## Requirements
- Python 3.x
- NumPy
- Matplotlib

You can install the required packages using:
```bash
pip install numpy matplotlib
```

---

## Installation Instructions

1. Clone the repository:
```bash
git clone https://github.com/mzohaibh17-pixel/Quantum_Wave_Packets_1D_2D.git
```

---

## Usage

Run the simulations using Python:

```bash
# Simulations (1D & 2D Combined Simulation)
python Quantum_Wave_Packets_1D_2D.py
```

---

## Outputs

The simulations generate the following plots and animations:

### 1D Wave Packet
- **Stationary states plot:**  
  ![1D Stationary States](plots/1D_stationary_states.png)  
- **Ground state probability density:**  
  ![1D Ground State](plots/1D_probability_ground.png)  
- **Initial wave packet probability density:**  
  ![1D Wave Packet](plots/1D_probability_t0.png)  
- **Time evolution animation:**  
  ![1D Wave Packet Animation](animations/1D_wave_packet.gif)  

### 2D Wave Packet
- **Single stationary state |ψ₄₄(x,y)|²:**  
  ![2D Stationary State](plots/2D_probability_4_4.png)  
- **Initial wave packet probability density:**  
  ![2D Wave Packet](plots/2D_wave_packet.png)  
- **Time evolution animation:**  
  ![2D Wave Packet Animation](animations/2D_wave_packet.gif)    

---

## Project Structure

Quantum_Wave_Packets_1D_2D/
 ├── Quantum_Wave_Packets_1D_2D.py
 ├── plots/
 ├── animations/
 ├── requirements.txt
 └── README.md

---

## References

- Griffiths, *Introduction to Quantum Mechanics*, 2nd Edition – for theory of quantum wavefunctions and particle in a box  
- Sakurai, *Modern Quantum Mechanics*, Revised Edition – for advanced quantum concepts  
- NumPy Documentation: [https://numpy.org/doc/](https://numpy.org/doc/) – for array computations and numerical operations in Python  
- Matplotlib Documentation: [https://matplotlib.org/stable/contents.html](https://matplotlib.org/stable/contents.html) – for plotting and creating animations in Python

---

## Author / Credits

**Muhammad Zohaib Hassan**  
- Bachelor’s in Physics, University of Sargodha  
- GitHub: [mzohaibh17-pixel](https://github.com/mzohaibh17-pixel)  
- Email: mzohaibh17@gmail.com  

*This project is for educational and research purposes in computational physics.*

