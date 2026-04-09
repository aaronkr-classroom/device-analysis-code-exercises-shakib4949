#Sensor.py
import random as r

class Sensor:
    """
    Base Sensor Class.
    """
    def __init__ (self, name: str)-> None:
        self.name= name
        
    def read(self) -> float:
        return 0.0  # to overwrite
    
#Inheritance
class TemperatureSensor (Sensor):
    """
    Simulated temp sensor.
    """
    def __init__(self,name: str)-> None:
        super().__init__(name)
        
    def read(self)-> float:  #Overwritten Sensor. read()
        return round(r.uniform(20.0, 30.0), 2)
    
class LightSensor(Sensor):
    """
    Simulated light Sensor.
    """
    
    def read(self) -> float:  #overwritten
        return round(r.uniform(0, 100),2)
    
    
    