class Temperature:
    def __init__(self, celsius):
        self.celsius = (float)(celsius)
        
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero (-273.15°C)")
        else:
            self._celsius = value
    
    @property
    def fahrenheit(self):
        return ((self.celsius * 9/5)+32)
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = (value - 32) * 5/9