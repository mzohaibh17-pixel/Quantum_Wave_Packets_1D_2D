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

**Files:**  
- `Quantum_Wave_Packets_1D_2D.py` → Python script containing all 1D and 2D simulations  
- `Plots/1D_stationary_states.png` → First three stationary states  
- `Plots/1D_probability_ground.png` → Ground state probability density  
- `Plots/1D_probability_t0.png` → Initial wave packet probability density  
- `Animations/1D_wavepacket.gif` → Animation of time evolution  

### 2D Simulations
- **Stationary Wavefunctions:** First few eigenstates ψₙₘ(x,y)  
- **Probability Density:** Ground state |ψ₁₁(x,y)|²  
- **Time-Dependent Wave Packet:** Superposition of first two states with animation showing |Ψ(x,y,t)|² over time  

**Files:**  
- `Plots/2D_stationary_states.png` → First few stationary states  
- `Plots/2D_probability_ground.png` → Ground state probability density  
- `Plots/2D_probability_t0.png` → Initial wave packet probability density  
- `Animations/2D_wavepacket.gif` → Animation of time evolution 

---

## Requirements
- Python 3.x
- NumPy
- Matplotlib

---

## Installation Instructions

1. Clone the repository:
```bash
git clone https://github.com/mzohaibh17-pixel/Quantum_Wave_Packets_1D_2D.git

---

## Usage

Run the simulations using Python:

```bash
# 1D simulation
python 1D_Wave_Packet_Time_Dependent.py

# 2D simulation
python 2D_Wave_Packet_Time_Dependent.py

---

## Outputs

The simulations generate both plots and animations:

### 1D Wave Packet
- Example plot:  
  ![1D Wave Packet Plot](Plots/1D_wave_packet.png)  
- Example animation:  
  ![1D Wave Packet Animation](Animations/1D_wave_packet.gif)  

### 2D Wave Packet
- Example plot:  
  ![2D Wave Packet Plot](Plots/2D_wave_packet.png)  
- Example animation:  
  ![2D Wave Packet Animation](Animations/2D_wave_packet.gif)  

---

## Project Structure

Quantum_Wave_Packets_1D_2D/
 ├── Quantum_Wave_Packets_1D_2D.py # Main simulation script
 ├── Plots/ # Contains static plots (PNG)
 ├── Animations/ # Contains animation files (GIF, MP4)
 ├── requirements.txt # Project dependencies
 └── README.md # Project documentation

---

## References

- Griffiths, *Introduction to Quantum Mechanics*, 2nd Edition  
- Sakurai, *Modern Quantum Mechanics*, Revised Edition  
- NumPy Documentation: [https://numpy.org/doc/](https://numpy.org/doc/)  
- Matplotlib Documentation: [https://matplotlib.org/stable/contents.html](https://matplotlib.org/stable/contents.html)

---

## Author / Credits

**Muhammad Zohaib Hassan**  
- Bachelor’s in Physics, University of Sargodha  
- GitHub: [mzohaibh17-pixel](https://github.com/mzohaibh17-pixel)  
- Email: mzohaibh17@gmail.com  

*This project is for educational and research purposes in computational physics.*

