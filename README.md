# Black Body Radiation Toolkit

This repository provides a collection of Python functions to **simulate, analyze, and visualize the radiation emitted by black bodies**, based on physical laws such as **Planck's Law** and **Wien's Displacement Law**.

It is designed for educational purposes and basic astrophysical analysis.

---

##  Features

-  Plot the spectral energy distribution of a black body at any temperature.
-  Compute the **peak wavelength** using **Wien’s Law**.
-  Calculate the **total radiated flux** by integrating Planck’s law.
-  Find the **fraction of energy** emitted in a custom wavelength range.
-  Classify a star approximately based on its temperature (spectral type).
-  Highlight common spectral bands (UV, visible, NIR, MIR) in plots.

---

##  Functions Overview

### `planck_law(T)`
Returns the Planck distribution for a black body at temperature `T` in CGS units.

### `wien_law(T)`
Returns the wavelength of maximum emission (in nm) using Wien's law.

### `energy(T)`
Integrates the Planck law over a wavelength range to compute the total flux (erg·s⁻¹·cm⁻²).

### `percentage_energy(T, lmbda1, lmbda2)`
Calculates the percentage of total flux emitted between two wavelengths (in nm).

### `plot_by_temperature(T)`
Plots the black body spectrum, highlights the peak, total flux, and spectral type.

### `plot_energy_in_a_range(T, lmbda1, lmbda2)`
Plots the spectrum and highlights a custom range, showing its energy contribution.

---

##  Requirements

This project requires the following Python libraries:

```bash
numpy
matplotlib
scipy
