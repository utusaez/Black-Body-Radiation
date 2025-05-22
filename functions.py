import numpy as np 
from scipy.integrate import quad


# Constants
c = 2.9979e10 # cm s^-1
kb = 1.3806e-16 # erg K^-1
h = 6.626e-27 # erg s^-1



def planck_law(T):

    """
    Calculates the Planck distribution function, describing the radiation emitted
    by a black body as a function of the wavelength and temperature, expressed in nanometers.

    PARAMETERS:
        
       T (float): Temperature of the black body in Kelvin
    
    RETURN:
        tuple:

        - wavelength (np.ndarray): Array of wavelenghts in nanometers.
        - planck_function_nm (np.ndarray): Spectral energy density (erg·s⁻¹·cm⁻²·nm⁻¹) for
        each wavelength

    Note:

        The internal function is calculated in CGS units and then is converted to nanometers multiplying by 1e-7.
    """

    wavelenght = np.linspace(1, 4000, 1000) #nm
    wavelenght_cm = wavelenght*1e-7

    planck_function = ((2*h*(c**2)) / (wavelenght_cm**5)) * (1 / (np.exp((h*c)/(wavelenght_cm*kb*T)) - 1))
    planck_function_nm = planck_function*1e-7

    return (wavelenght, planck_function_nm)



def wien_law(T):

    """
    Calculates the wavelength at which a black body emits maximun radiation at a given
    temperature, using Wien's displacement law.

    PARAMETERS:

        T (float): Temperature of the black body in Kelvin
    
    RETURN:

        float: wavelength (in nanometers) corresponding to the peak of emission.

    Note:

        The Wien's constant used is 0.2898 cm·K. The result is converted from cm to nm.
    """

    lambda_max = 0.2898/T # cm
    return lambda_max*1e7 # nm y K



def energy(T):

    """ 
    Calculates the total energy emitted per unit of area, per unit of time and per unit of surface
    (energetic flux) by a black body at temperature T, by integrating the Planck's law expressed in 
    terms of an adimensional variable over the entire wavelength range.

    PARAMETERS:

        T (float): Temperature of the black body in Kelvin

    RETURN:

        float: Total energy integrated over all wavelengths, in erg·s⁻¹·cm⁻².

    Notes:

        - The integration uses the adimensional form of Planck's law, where the integration 
          variable x = (h*c) / (λ*k_B*T).
        - The integral is performed from 0 to infinity in terms of x.
        - The constant factor outside the integral converts the adimensional integral back to 
        physical units, assuming CGS units for constants.

    """
    constant = (2*((kb*T)**4)) / ((h**3)*(c**2))
    
    def adimensional_function(x, T):

        adimensional_function = (x**3) / (np.exp(x) - 1)
        return adimensional_function

    energy_planck, error_planck = quad(adimensional_function, 0, np.inf, args=(T,)) #erg cm^−2 s^−1
    energy_planck = np.pi*constant*energy_planck

    return energy_planck



def percentage_energy(T, lmbda1, lmbda2):

    """
    Calculates the percentage of the total flux emitted by a black body at temperature T 
    that lies within a specific wavelength range, using the adimensional form of Planck's law.

    PARAMETERS:

        - T (float): Temperature of the black body in Kelvin.
        - lmbda1 (float): Lower limit of the wavelength in nanometers.
        - lmbda2 (float): Upper limit of the wavelength in nanometers.

    RETURN:

        float: Percentage of total emitted flux that lies between lmbda1 and lmbda2 (in %).

    Notes:

        - The Planck function is expressed in terms of the adimensional variable 
          x = (h*c)/(λ*k_B*T), and the integration is performed over x1 to x2.
        - The physical wavelength limits are converted to adimensional x-limits 
          before integration.
        - The result is normalized with respect to the total flux computed from 
          the full integral (0 to infinity) in adimensional form.
        - All constants are in CGS units, and the final result is a dimensionless 
          percentage. 

    """

    lmbda1_cm, lmbda2_cm = lmbda1*1e-7, lmbda2*1e-7

    constant = (2*((kb*T)**4)) / ((h**3)*(c**2))
    
    def adimensional_function(x, T):

        adimensional_function = (x**3) / (np.exp(x) - 1)
        return adimensional_function
    
    x1 = (h*c) / (lmbda2_cm * kb * T) 
    x2 = (h*c) / (lmbda1_cm * kb * T)

    energy_planck_range, error_planck_range = quad(adimensional_function, x1, x2, args=(T,)) #erg cm^−2 s^−1
    
    energy_fraction = (np.pi*constant*energy_planck_range / energy(T)) * 100
    
    return round(energy_fraction, 4)
