import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.constants import mu_0
from tkinter import font as tkfont

def calculate_resonant_frequency(L, C):
    return 1 / (2 * math.pi * math.sqrt(L * C))

def select_standard(value, list):
    distances = []
    for standard_width in list:
        distance = calculate_distance(value, standard_width)
        distances.append(distance)
    index_selected_width = distances.index(min(distances))
    #real_distance = value - list[index_selected_width]
    #if real_distance > 0:
    #    index_selected_width = index_selected_width + 1
    width = list[index_selected_width]
    return width

def calculate_distance(point1, point2):
    distance = abs(point2 - point1)
    return distance

def resonant_frequency(L, C):
    return 1 / (2 * math.pi * math.sqrt(L * C))

def calculate_inductance_resonant(f_res, C):
    return 1 / ((2 * math.pi * f_res) ** 2 * C)

def oscillator_frequency(R, C):
    return 1 / (2 * math.pi * R * C)

def calculate_resistance_oscillator(f, C):
    return 1 / (2 * math.pi * f * C)

def good(hello):
    # Remove duplicates
    unique_resistance_values = list(set(hello))

    # Sort the list
    sorted_resistance_values = sorted(unique_resistance_values)
    return sorted_resistance_values

resistance_values = [
    # mΩ values
    1.0e-3, 1.5e-3, 2.2e-3, 3.3e-3, 4.7e-3, 6.8e-3,
    # E6 Series
    1.0, 1.5, 2.2, 3.3, 4.7, 6.8,
    # E12 Series
    1.0, 1.2, 1.5, 1.8, 2.2, 2.7, 3.3, 3.9, 4.7, 5.6, 6.8, 8.2,
    # E24 Series
    1.0, 1.1, 1.2, 1.3, 1.5, 1.6, 1.8, 2.0, 2.2, 2.4, 2.7, 3.0, 3.3,
    3.6, 3.9, 4.3, 4.7, 5.1, 5.6, 6.2, 6.8, 7.5, 8.2, 9.1,
    # E48 Series
    1.0, 1.05, 1.1, 1.15, 1.21, 1.27, 1.33, 1.4, 1.47, 1.54, 1.62,
    1.69, 1.78, 1.87, 1.96, 2.05, 2.15, 2.26, 2.37, 2.49, 2.61, 2.74,
    2.87, 3.01, 3.16, 3.32, 3.48, 3.65, 3.83, 4.02, 4.22, 4.42, 4.64,
    4.87, 5.11, 5.36, 5.62, 5.9, 6.19, 6.49, 6.81, 7.15, 7.5, 7.87,
    8.25, 8.66, 9.09,
    # Kiloohms
    1.0e3, 1.5e3, 2.2e3, 3.3e3, 4.7e3, 6.8e3, 10.0e3, 15.0e3, 22.0e3, 33.0e3, 47.0e3, 68.0e3,
    100.0e3, 150.0e3, 220.0e3, 330.0e3, 470.0e3, 680.0e3,
    1.0e6, 1.5e6, 2.2e6, 3.3e6, 4.7e6, 6.8e6,
    10.0e6, 15.0e6, 22.0e6, 33.0e6, 47.0e6, 68.0e6,
    100.0e6, 150.0e6, 220.0e6, 330.0e6, 470.0e6, 680.0e6,
    1.0e9, 1.5e9, 2.2e9, 3.3e9, 4.7e9, 6.8e9,
    # Megaohms
    1.0e6, 1.5e6, 2.2e6, 3.3e6, 4.7e6, 6.8e6,
    # Gigaohms
    1.0e9, 1.5e9, 2.2e9, 3.3e9, 4.7e9, 6.8e9
]
resistance_values = good(resistance_values)

inductance_values = [
    # E6 Series
    1.0e-9, 1.5e-9, 2.2e-9, 3.3e-9, 4.7e-9, 6.8e-9,
    # E12 Series
    1.0e-9, 1.2e-9, 1.5e-9, 1.8e-9, 2.2e-9, 2.7e-9, 3.3e-9, 3.9e-9, 4.7e-9, 5.6e-9, 6.8e-9, 8.2e-9,
    # E24 Series
    1.0e-9, 1.1e-9, 1.2e-9, 1.3e-9, 1.5e-9, 1.6e-9, 1.8e-9, 2.0e-9, 2.2e-9, 2.4e-9, 2.7e-9, 3.0e-9, 3.3e-9,
    3.6e-9, 3.9e-9, 4.3e-9, 4.7e-9, 5.1e-9, 5.6e-9, 6.2e-9, 6.8e-9, 7.5e-9, 8.2e-9, 9.1e-9,
    # E48 Series
    1.0e-9, 1.05e-9, 1.1e-9, 1.15e-9, 1.21e-9, 1.27e-9, 1.33e-9, 1.4e-9, 1.47e-9, 1.54e-9, 1.62e-9,
    1.69e-9, 1.78e-9, 1.87e-9, 1.96e-9, 2.05e-9, 2.15e-9, 2.26e-9, 2.37e-9, 2.49e-9, 2.61e-9, 2.74e-9,
    2.87e-9, 3.01e-9, 3.16e-9, 3.32e-9, 3.48e-9, 3.65e-9, 3.83e-9, 4.02e-9, 4.22e-9, 4.42e-9, 4.64e-9,
    4.87e-9, 5.11e-9, 5.36e-9, 5.62e-9, 5.9e-9, 6.19e-9, 6.49e-9, 6.81e-9, 7.15e-9, 7.5e-9, 7.87e-9,
    8.25e-9, 8.66e-9, 9.09e-9,
    # µH values
    1.0e-6, 1.5e-6, 2.2e-6, 3.3e-6, 4.7e-6, 6.8e-6,
    1.0e-6, 1.2e-6, 1.5e-6, 1.8e-6, 2.2e-6, 2.7e-6, 3.3e-6, 3.9e-6, 4.7e-6, 5.6e-6, 6.8e-6, 8.2e-6,
    1.0e-6, 1.1e-6, 1.2e-6, 1.3e-6, 1.5e-6, 1.6e-6, 1.8e-6, 2.0e-6, 2.2e-6, 2.4e-6, 2.7e-6, 3.0e-6, 3.3e-6,
    3.6e-6, 3.9e-6, 4.3e-6, 4.7e-6, 5.1e-6, 5.6e-6, 6.2e-6, 6.8e-6, 7.5e-6, 8.2e-6, 9.1e-6,
    # More µH values
    10e-6, 12e-6, 15e-6, 18e-6, 22e-6, 27e-6, 33e-6, 39e-6, 47e-6, 56e-6, 68e-6, 82e-6,
    100e-6, 120e-6, 150e-6, 180e-6, 220e-6, 270e-6, 330e-6, 390e-6, 470e-6, 560e-6, 680e-6, 820e-6,
    1.0e-3, 1.2e-3, 1.5e-3, 1.8e-3, 2.2e-3, 2.7e-3, 3.3e-3, 3.9e-3, 4.7e-3, 5.6e-3, 6.8e-3, 8.2e-3,
    10e-3, 12e-3, 15e-3, 18e-3, 22e-3, 27e-3, 33e-3, 39e-3, 47e-3, 56e-3, 68e-3, 82e-3,
    100e-3, 120e-3, 150e-3, 180e-3, 220e-3, 270e-3, 330e-3, 390e-3, 470e-3, 560e-3, 680e-3, 820e-3,
    1.0, 1.2, 1.5, 1.8, 2.2, 2.7, 3.3, 3.9, 4.7, 5.6, 6.8, 8.2,
    10, 12, 15, 18, 22, 27, 33, 39, 47, 56, 68, 82,
    100, 120, 150, 180, 220, 270, 330, 390, 470, 560, 680, 820
]
inductance_values = good(inductance_values)

capacitor_values = [
    1e-12,   # 1 pF
    10e-12,  # 10 pF
    100e-12, # 100 pF
    220e-12, # 220 pF
    470e-12, # 470 pF
    1e-9,    # 1 nF
    10e-9,   # 10 nF
    22e-9,   # 22 nF
    47e-9,   # 47 nF
    100e-9,  # 100 nF
    220e-9,  # 220 nF
    470e-9,  # 470 nF
    1e-6,    # 1 µF
    10e-6,   # 10 µF
    22e-6,   # 22 µF
    47e-6,   # 47 µF
    100e-6,  # 100 µF
    220e-6,  # 220 µF
    470e-6,  # 470 µF
    1e-3,    # 1 mF
    1e+12    # Means the value out of range
]
capacitor_values = good(capacitor_values)

desired_frequency = 10000

print(f'The desired frequency is: {desired_frequency*1e-3:.4} KHz')
C1 = 10*1e-6# Oscillator circuit Farads

C2 = 10*1e-6# Resonance circuit Farads

if C1 in capacitor_values:
    print(f'C_osc = {C1:.4} F - The chosen capacitor is standard')
else:
    print(print(f'C_osc = {C1:.4} F - The chosen capacitor is not standard'))

# Selecting the standard resistance for oscillating circuit
R_osc = calculate_resistance_oscillator(desired_frequency, C1)
R_osc_standard = select_standard(R_osc, resistance_values)
print(f'R_osc: {R_osc*1e-3:.4} KOhm - Standard R_osc = {R_osc_standard*1e-3:.4} KOhm')
standard_oscillating_frequency = oscillator_frequency(R_osc_standard, C1)
standard_oscillating_frequency = 1
# Resonant circuit
L_resonance = calculate_inductance_resonant(standard_oscillating_frequency, C2)
L_resonance_standard = select_standard(L_resonance, inductance_values)
Resonant_freq = resonant_frequency(L_resonance_standard, C2)
print(L_resonance, 'heeere')
if C2 in capacitor_values:
    print(f'C_res = {C2:.4} F - The chosen capacitor is standard')
else:
    print(print(f'C_res ={C2:.4} F - The chosen capacitor is not standard'))

print(f'\nThe oscillating circuit: R_osc={R_osc_standard*1e-3:.4} KOhm - C_osc={C1*1e6:.4} uF - f_osc= {standard_oscillating_frequency*1e-3:.4} KHz')
print(f'The resonant circuit: L_res={L_resonance*1e6:.6} uH - C_res={C2*1e6:.6} uF - f={Resonant_freq*1e-3:.4} KHz')
print(f'Difference in freq: {(standard_oscillating_frequency-Resonant_freq):.4} Hz')

print(f'{(resonant_frequency(26.7e-6, 10*1e-9) * 1e-3):.5} KHz')
print(f'{oscillator_frequency(75, 10*1e-9) * 1e-3 :.5} KHz')