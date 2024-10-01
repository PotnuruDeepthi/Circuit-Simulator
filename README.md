# Circuit-Simulator
A python based circuit simulator..


# RLC Circuit Simulator

This RLC Circuit Simulator is a Python application that allows users to calculate and visualize the behavior of a series RLC circuit. The application provides a graphical user interface (GUI) for inputting circuit parameters and generates voltage and current waveforms based on user-defined values.

## Features

-   Input Parameters  : Users can input resistance (R), inductance (L), capacitance (C), frequency (f), and voltage (V) to simulate the circuit.
-   Impedance Calculation  : The simulator calculates the total impedance of the circuit based on the input parameters.
-   Current Calculation  : It computes the current flowing through the circuit using the applied voltage and impedance.
-   Waveform Visualization  : The application plots the voltage and current waveforms, providing a visual representation of the circuit's behavior over time.
-   User-Friendly GUI  : Built using Tkinter, the application offers an intuitive interface for ease of use.

## Requirements

To run this simulator, ensure you have the following Python packages installed:

- `tkinter`: For the GUI interface (comes with standard Python installations)
- `numpy`: For numerical calculations
- `matplotlib`: For plotting the waveforms

You can install the required packages using pip:

```bash
pip install numpy matplotlib
```

## How to Use

1. Run the application:
   ```bash
   python rlc_circuit_simulator.py
   ```

2. Enter the values for:
   - Resistance (R) in ohms
   - Inductance (L) in henries
   - Capacitance (C) in farads
   - Frequency (f) in Hz
   - Voltage (V) in volts

3. Click the "Simulate" button to calculate the impedance, current, and phase angle. The results will be displayed on the screen.

4. The voltage and current waveforms will be plotted in a separate window for visualization.

## Example Input/Output

  Inputs:  
- R: 15 Ω
- L: 0.01 H
- C: 0.0002 F
- f: 100 Hz
- V: 5 V

  Outputs:  
- Impedance: 15 - j1.68  Ω
- Current: approx 0.331  A
- Phase Angle: approx -6.38°
  ![Screenshot (186)](https://github.com/user-attachments/assets/5cc03488-c9dc-44ff-a9ff-a27b62250861)


