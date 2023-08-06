"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature: float, neutrons_emitted: float):
    """Verify criticality is balanced.

    The first thing a control system has to do is check if the reactor is balanced in criticality.
A reactor is said to be critical if it satisfies the following conditions:

- The temperature is less than 800 K.
- The number of neutrons emitted per second is greater than 500.
- The product of temperature and neutrons emitted per second is less than 500000.

    Implement the function `is_criticality_balanced()` that takes `temperature` measured in kelvin and 
    `neutrons_emitted` as parameters, and returns `True` if the criticality conditions are met, `False` if not.

    :param temperature: int or float - temperature value in kelvin.
    :param neutrons_emitted: int or float - number of neutrons emitted per second.
    :return: bool - is criticality balanced?

    A reactor is said to be critical if it satisfies the following conditions:
    - The temperature is less than 800 K.
    - The number of neutrons emitted per second is greater than 500.
    - The product of temperature and neutrons emitted per second is less than 500000.
    """
    CRITICAL_TEMPERATURE = 800
    CRITICAL_EMITTED_NEUTRONS = 500
    CRITICAL_PRODUCT = 500000

    product = temperature * neutrons_emitted

    if temperature >= CRITICAL_TEMPERATURE or neutrons_emitted <= CRITICAL_EMITTED_NEUTRONS:
        return False
    return product < CRITICAL_PRODUCT

    

def reactor_efficiency(voltage: float, current: float, theoretical_max_power: float) -> str:
    """Assess reactor efficiency zone.

    :param voltage: int or float - voltage value.
    :param current: int or float - current value.
    :param theoretical_max_power: int or float - power that corresponds to a 100% efficiency.
    :return: str - one of ('green', 'orange', 'red', or 'black').

    Efficiency can be grouped into 4 bands:

    1. green -> efficiency of 80% or more,
    2. orange -> efficiency of less than 80% but at least 60%,
    3. red -> efficiency below 60%, but still 30% or more,
    4. black ->  less than 30% efficient.

    The percentage value is calculated as
    (generated power/ theoretical max power)*100
    where generated power = voltage * current
    """

    efficency = ((voltage * current) / theoretical_max_power) * 100
    return 'green' if efficency >= 80 else 'orange' if efficency >= 60 else 'red' if efficency >= 30 else 'black'



def fail_safe(temperature: float, neutrons_produced_per_second: float, threshold: float) -> str: 
    """Assess and return status code for the reactor.

    :param temperature: int or float - value of the temperature in kelvin.
    :param neutrons_produced_per_second: int or float - neutron flux.
    :param threshold: int or float - threshold for category.
    :return: str - one of ('LOW', 'NORMAL', 'DANGER').

    1. 'LOW' -> `temperature * neutrons per second` < 90% of `threshold`
    2. 'NORMAL' -> `temperature * neutrons per second` +/- 10% of `threshold`
    3. 'DANGER' -> `temperature * neutrons per second` is not in the above-stated ranges
    """

    criticality = temperature * neutrons_produced_per_second
    percent = criticality * 100 / threshold

    return 'LOW' if percent < 90 else 'NORMAL' if 90 <= percent <= 110 else 'DANGER'

 
 