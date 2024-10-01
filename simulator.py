import tkinter as tk
from tkinter import messagebox
import math
import numpy as np
import matplotlib.pyplot as plt

# Function to calculate impedance in a series RLC circuit
def calculate_impedance(R, L, C, f):
    omega = 2 * math.pi * f
    X_L = omega * L
    X_C = 1 / (omega * C)
    Z = complex(R, X_L - X_C)
    return Z

# Function to calculate current in the circuit
def calculate_current(V, Z):
    I = V / Z
    return I

# Function to plot the voltage and current waveforms
def plot_waveforms(V, I_mag, f, phase_angle):
    t = np.linspace(0, 1/f, 1000)  # Time values for one period
    voltage_waveform = V * np.sin(2 * np.pi * f * t)  # Voltage waveform
    current_waveform = I_mag * np.sin(2 * np.pi * f * t + math.radians(phase_angle))  # Current waveform
    
    plt.figure()
    plt.plot(t, voltage_waveform, label="Voltage (V)")
    plt.plot(t, current_waveform, label="Current (I)", linestyle="--")
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title(f'Voltage and Current Waveforms (f = {f} Hz)')
    plt.legend()
    plt.grid(True)
    plt.show()

# Function to simulate circuit and update results
def simulate_circuit():
    try:
        # Get values from input fields
        R = float(entry_R.get())
        L = float(entry_L.get())
        C = float(entry_C.get())
        f = float(entry_f.get())
        V = float(entry_V.get())
        
        # Calculate impedance and current
        Z = calculate_impedance(R, L, C, f)
        I = calculate_current(V, Z)
        
        # Update result labels
        result_impedance.config(text=f"Impedance: {Z:.2f} ohms")
        result_current.config(text=f"Current: {abs(I):.2f} A")
        phase_angle = math.degrees(math.atan2(I.imag, I.real))
        result_phase.config(text=f"Phase Angle: {phase_angle:.2f} degrees")
        
        # Plot waveforms
        plot_waveforms(V, abs(I), f, phase_angle)
    
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numeric values.")

# Create the main window
root = tk.Tk()
root.title("RLC Circuit Simulator with Graphs")

# Create labels and input fields for R, L, C, f, V
tk.Label(root, text="Resistance (R) in ohms:").grid(row=0, column=0, padx=10, pady=5)
entry_R = tk.Entry(root)
entry_R.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Inductance (L) in henries:").grid(row=1, column=0, padx=10, pady=5)
entry_L = tk.Entry(root)
entry_L.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Capacitance (C) in farads:").grid(row=2, column=0, padx=10, pady=5)
entry_C = tk.Entry(root)
entry_C.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Frequency (f) in Hz:").grid(row=3, column=0, padx=10, pady=5)
entry_f = tk.Entry(root)
entry_f.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Voltage (V) in volts:").grid(row=4, column=0, padx=10, pady=5)
entry_V = tk.Entry(root)
entry_V.grid(row=4, column=1, padx=10, pady=5)

# Create a button to simulate the circuit
simulate_button = tk.Button(root, text="Simulate", command=simulate_circuit)
simulate_button.grid(row=5, column=0, columnspan=2, pady=10)

# Create labels to display the results
result_impedance = tk.Label(root, text="Impedance: ")
result_impedance.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

result_current = tk.Label(root, text="Current: ")
result_current.grid(row=7, column=0, columnspan=2, padx=10, pady=5)

result_phase = tk.Label(root, text="Phase Angle: ")
result_phase.grid(row=8, column=0, columnspan=2, padx=10, pady=5)

# Start the Tkinter main loop
root.mainloop()
