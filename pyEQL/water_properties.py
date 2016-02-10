'''
pyEQL water properties library

This file contains functions for retrieving various physical properties
of water substance

:copyright: 2013-2016 by Ryan S. Kingsbury
:license: LGPL, see LICENSE for more details.

'''
import math

from pyEQL import unit

# logging system
import logging
logger = logging.getLogger(__name__)

# add a filter to emit only unique log messages to the handler
import pyEQL.logging_system
unique = pyEQL.logging_system.Unique()
logger.addFilter(unique)

# add a handler for console output, since pyEQL is meant to be used interactively
ch = logging.StreamHandler()

# create formatter for the log
formatter = logging.Formatter('(%(name)s) - %(levelname)s - %(message)s')

# add formatter to the handler
ch.setFormatter(formatter)
logger.addHandler(ch)

def water_density(temperature=25*unit('degC'),pressure=1*unit('atm')):
    '''    
    Return the density of water in kg/m3 at the specified temperature and pressure.
    
    Parameters
    ----------
    temperature : float or int, optional
                  The temperature in Celsius. Defaults to 25 degrees if not specified.
    pressure    : float or int, optional
                  The ambient pressure of the solution in Pascals (N/m2). 
                  Defaults to atmospheric pressure (101325 Pa) if not specified.
    
    Returns
    -------
    float
            The density of water in kg/m3.
    
    Notes
    -----
    Based on IAPWS95 model <http://www.iapws.org/release.html>

    
    '''
    # call IAPWS. The density is returned in kg/m**3 units
    # IAPWS expects temperature in K and pressure in MPa, so convert the units
    from iapws import IAPWS95
    h2o = IAPWS95(P=pressure.to('MPa').magnitude,T=temperature.to('K').magnitude)
    density = h2o.rho * unit('kg/m**3')
    
    logger.info('Computed density of water as %s at T= %s and P = %s' % (density,temperature,pressure))
    logger.debug('Computed density of water using the IAPWS95 standard')
    
    return density.to('kg/m**3')
    
def water_specific_weight(temperature=25*unit('degC'),pressure=1*unit('atm')):
    '''    
    Return the specific weight of water in N/m3 at the specified temperature and pressure.
    
    Parameters
    ----------
    temperature : Quantity, optional
                  The temperature. Defaults to 25 degC if omitted.
    pressure    : Quantity, optional
                  The ambient pressure of the solution. 
                  Defaults to atmospheric pressure (1 atm) if omitted.
                  
    Returns
    -------
    Quantity
            The specific weight of water in N/m3.  
    
    Examples
    --------
    >>> water_specific_weight() #doctest: +ELLIPSIS
    <Quantity(9777.637025975, 'newton / meter ** 3')>
            
    See Also
    --------
    water_density
    
    '''
    spweight = water_density(temperature,pressure) * unit.g_n
    logger.info('Computed specific weight of water as %s at T=%s and P = %s' % (spweight,temperature,pressure))
    return spweight.to('N/m ** 3')

def water_viscosity_dynamic(temperature=25*unit('degC'),pressure=1*unit('atm')):
    '''
    Return the dynamic (absolute) viscosity of water in N-s/m2 = Pa-s = kg/m-s
    at the specified temperature.
    
    Parameters
    ----------
    temperature : Quantity, optional
                  The temperature. Defaults to 25 degC if omitted.
    pressure    : Quantity, optional
                  The ambient pressure of the solution. 
                  Defaults to atmospheric pressure (1 atm) if omitted.
    
    Returns
    -------
    Quantity 
                The dynamic (absolute) viscosity of water in N-s/m2 = Pa-s = kg/m-s
                  
    Notes
    -----
    Based on IAPWS95 model <http://www.iapws.org/release.html>
    
    '''
    # call IAPWS. The viscosity is returned in Pa*s units
    # IAPWS expects temperature in K and pressure in MPa, so convert the units
    from iapws import IAPWS95
    h2o = IAPWS95(P=pressure.to('MPa').magnitude,T=temperature.to('K').magnitude)
    viscosity = h2o.mu * unit('Pa * s')
    
    logger.info('Computed dynamic (absolute) viscosity of water as %s at T=%s and P = %s'  % (viscosity,temperature,pressure)) 
    
    logger.debug('Computed dynamic (absolute) viscosity of water using the IAPWS95 standard')
    
    return viscosity.to('kg/m/s')


def water_viscosity_kinematic(temperature=25*unit('degC'),pressure=1*unit('atm')):
    '''
    Return the kinematic viscosity of water in m2/s = Stokes
    at the specified temperature and pressure.
    
    Parameters
    ----------
    temperature : Quantity, optional
                  The temperature. Defaults to 25 degC if omitted.
    pressure    : Quantity, optional
                  The ambient pressure of the solution. 
                  Defaults to atmospheric pressure (1 atm) if omitted.
                  
    Returns
    -------
    Quantity
            The kinematic viscosity of water in Stokes (m2/s)

    Notes
    -----
    Based on IAPWS95 model <http://www.iapws.org/release.html>
    
    '''
    # call IAPWS. The kinematic viscosity is returned in m**2/s units
    # IAPWS expects temperature in K and pressure in MPa, so convert the units
    from iapws import IAPWS95
    h2o = IAPWS95(P=pressure.to('MPa').magnitude,T=temperature.to('K').magnitude)
    kviscosity = h2o.nu * unit('m**2/s')
    
    logger.info('Computed kinematic viscosity of water as %s at T=%s and P = %s ' % (kviscosity,temperature,pressure)) 
    
    logger.debug('Computed kinematic viscosity of water using the IAPWS95 standard.')
    
    return kviscosity.to('m**2 / s')
    

def water_dielectric_constant(temperature=25*unit('degC'),pressure=1*unit('atm')):
    '''    
    Return the dielectric constant of water at the specified temperature and pressure.
    
    Parameters
    ----------
    temperature : Quantity, optional
                  The temperature. Defaults to 25 degC if omitted.
    pressure    : Quantity, optional
                  The ambient pressure of the solution. 
                  Defaults to atmospheric pressure (1 atm) if omitted.
                  
    Returns
    -------
    float
            The dielectric constant (or permittivity) of water relative to the
            permittivity of a vacuum. Dimensionless.
    
    Notes
    -----
    Based on the IAPWS95 standard <http://www.iapws.org/release.html>
     
    '''
    # call IAPWS. The returned dielectric constant has no units.
    # IAPWS expects temperature in K and pressure in MPa, so convert the units
    from iapws import IAPWS95
    h2o = IAPWS95(P=pressure.to('MPa').magnitude,T=temperature.to('K').magnitude)
    dielectric = h2o.epsilon
    
    logger.info('Computed dielectric constant of water as %s at T=%s and P = %s' % (dielectric,temperature,pressure))
    
    logger.debug('Computed dielectric constant of water using the IAPWS95 standard.')
    
    return dielectric
    
def water_conductivity(temperature):
    pass

# TODO - turn doctest back on when the nosigint error is gone        
if __name__ == "__main__":
    import doctest
    doctest.testmod()
