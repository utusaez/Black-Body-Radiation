import matplotlib.pyplot as plt
import numpy as np
import functions as fun




def plot_by_temperature(T):

    """ 
    Plots the Planck's law at a given temperature and displays key information
    about the black body spectrum corresponding to a star.

    PARAMETERS:

        - T (float): Temperature of the black body (star) in Kelvin.

    Notes:

        The function generates a plot of the spectral flux according to the Planck's law as
        a function of wavelength (in nanometers) for a giventemperature T. Additionally:

            - Shows the peak wavelength obtained using Wien's law
            - Calculates and displays the total total emitted energy flux.
            - Classifies the star approximately according to its spectral type (O, B, A, F, G, K, M).

        The curve is expressed in CGS units:
            - Wavelength in nanometers (nm)
            - Flux in erg s⁻¹ cm⁻² cm⁻¹.
    """

    if T >= 30000:
        type_star = "O"
    elif 30000 > T and T >= 10000:
        type_star = "B"
    elif 10000 > T and T >= 7500:
        type_star = "A"
    elif 7500 > T and T >= 6000:
        type_star = "F"
    elif 6000 > T and T >= 5000:
        type_star = "G"
    elif 5000 > T and T >= 3500:
        type_star = "K"
    elif 3500 > T and T >= 2500:
        type_star = "M"

    fig, ax = plt.subplots(figsize=(12, 8))
    ax.plot(fun.planck_law(T)[0], fun.planck_law(T)[1] , color = "#005f99", label = f"Temperature: {T} (K)")
    ax.axvline(fun.wien_law(T), ls = "--", color = "#005f99", label = f"Max wavelenght: {fun.wien_law(T):.3e} (nm)")
    ax.plot([], [], ' ', label = rf"Energy: {fun.energy(T):.4e} (erg cm$^{-2}$ s$^{-1})$")
    ax.plot([], [], ' ', label = f"Type star: {type_star}")

    ax.set_xlabel(r"$\mathrm{Wavelength} \ (\mathrm{nm})$")
    ax.set_ylabel(r"$F_\lambda \ (\mathrm{erg\,s^{-1}\,cm^{-2}\,cm^{-1}})$")
    ax.grid()
    ax.legend(fontsize = 12)
    plt.show()



def plot_energy_in_a_range(T, lmbda1, lmbda2):

    """ 
    Plots the black body spectrum  for a given temperature T, highlighting the wavelength range
    of interest and displaying the fraction of energy emitted in that range.

    PARAMETERS:

        - T (float): Temperature of the black body in Kelvin.
        - lmbda1 (float): Lower limit of the spectrum range (in nanometers).
        - lmbda2 (float): Upper limit of the spectrum range (in nanometers).

    Notes:

        This function generates a plot of the spectral flux according to the Planck's law for a
        given temperature T, highlighting the region between lmbda1 and lmbda2 with vertical lines.

    Additionally:
        - Displays the fraction of the total emitted flux within the defined range.
        - Classifies the star approximately according its spectral type (O, B, A, F, G, K, M).
        - Shades characteristic spectral bands:
            Ultraviolet (UV), visible, Near infrared (NIR) and Mid infrared (MIR).

    Units follows the CGS system:
        - Wavelength: nanometers (nm).
        - Spectral flux: erg s⁻¹ cm⁻² cm⁻¹.
    """

    if T >= 30000:
        type_star = "O"
    elif 30000 > T and T >= 10000:
        type_star = "B"
    elif 10000 > T and T >= 7500:
        type_star = "A"
    elif 7500 > T and T >= 6000:
        type_star = "F"
    elif 6000 > T and T >= 5000:
        type_star = "G"
    elif 5000 > T and T >= 3500:
        type_star = "K"
    elif 3500 > T and T >= 2500:
        type_star = "M"

    fig, ax = plt.subplots(figsize=(12, 8))
    ax.plot(fun.planck_law(T)[0], fun.planck_law(T)[1] , color = "#005f99", label = f"Temperature: {T} (K)")
    ax.plot([], [], ' ', label=f"Fraction of Energy: {fun.percentage_energy(T, lmbda1, lmbda2)} %")
    ax.plot([], [], ' ', label=f"Type star: {type_star}")

    ax.axvspan(10, 400, color='purple', alpha = 0.13)
    ax.axvspan(400, 780, color='green', alpha = 0.13)
    ax.axvspan(780, 2500, color='red', alpha = 0.13)
    ax.axvspan(2500, 4000, color='red', alpha = 0.2)

    ax.axvline(lmbda1, ls = "--", color = "gray")
    ax.axvline(lmbda2, ls = "--", color = "gray")

    ax.text(205, 0.45e6, "UV", ha='center', va='bottom', fontsize=15, alpha=0.8)
    ax.text(590, 0.45e6, "Visible", ha='center', va='bottom', fontsize=15, alpha=0.8)
    ax.text(1640, 0.45e6, "NIR", ha='center', va='bottom', fontsize=15, alpha=0.8)
    ax.text(3250, 0.45e6, "MIR", ha='center', va='bottom', fontsize=15, alpha=0.8)

    ax.set_xlabel(r"$\mathrm{Wavelength} \ (\mathrm{nm})$")
    ax.set_ylabel(r"$F_\lambda \ (\mathrm{erg\,s^{-1}\,cm^{-2}\,cm^{-1}})$")
    ax.grid()
    ax.legend(fontsize = 12)
    plt.show() 
