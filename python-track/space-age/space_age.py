"""Instruction:

Given an age in seconds, calculate how old someone would be on:
- Mercury: orbital period 0.2408467 Earth years
- Venus: orbital period 0.61519726 Earth years
- Earth: orbital period 1.0 Earth years, 365.25 Earth days, or 31557600 seconds
- Mars: orbital period 1.8808158 Earth years
- Jupiter: orbital period 11.862615 Earth years
- Saturn: orbital period 29.447498 Earth years
- Uranus: orbital period 84.016846 Earth years
- Neptune: orbital period 164.79132 Earth years
"""

class SpaceAge:
    def __init__(self, seconds: int):
        self.age_as_seconds = seconds
        self.year_to_seconds: int = 31557600
        self.orbital_periods = {
            "mercury":  0.2408467,
            "venus":    0.61519726,
            "earth":    1.0,
            "mars":     1.8808158,
            "jupiter":  11.862615,
            "saturn":   29.447498,
            "uranus":   84.016846,
            "neptune":  164.79132
        }
        
    def calculate_age(self, planet: str) -> float:
        """Calculates the age on a specific planet.
        
        Args:
        orbital_period (float): The orbital period of the planet in Earth years.

        Returns:
        float: The age on the specific planet, rounded to two decimal places.
        """
        orbital_period = self.orbital_periods[planet.lower()]
        return round(self.age_as_seconds / (orbital_period * self.year_to_seconds), 2)
            
    def on_mercury(self) -> float:
        return self.calculate_age("mercury") 
        
    def on_venus(self) -> float:
        return self.calculate_age("venus") 
        
    def on_earth(self) -> float:
        return self.calculate_age("earth") 
        
    def on_mars(self) -> float:
        return self.calculate_age("mars") 
        
    def on_jupiter(self) -> float:
        return self.calculate_age("jupiter") 
        
    def on_saturn(self) -> float:
        return self.calculate_age("saturn") 
        
    def on_uranus(self) -> float:
        return self.calculate_age("uranus") 
        
    def on_neptune(self) -> float:
        return self.calculate_age("neptune") 
