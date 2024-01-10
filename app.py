
# передавальне відношення в дюймах (gear_inches).
# Для його обчислення використовується така формула:
#   gear_inches = діаметр колеса (wheel_diameter) × передавальне відношення (gear_ratio),
# де
# wheel_diameter (діаметр колеса) = 
#       діаметр обода (rim_diameter) + подвійний діаметр (висота) шини (twice_tire_diameter)

class Bicycle:
    
    def __init__(self):
        self.front_wheel = None
        self.rear_wheel = None
        self.gear = None
    
    """
    params:
        type - "f"-fron or "r"-rear
        rim_diameter - rim diameter in inches
        tire_height - tire height in inches 
    """
    def setup_wheel(self, type: str, rim_diameter: float, tire_height: float):
        
        if type == "f":
            self.front_wheel = Wheel(rim_diameter, tire_height)
        elif type == "r":
            self.rear_wheel = Wheel(rim_diameter, tire_height)
    
    def setup_gear(self, chainring: int, cog: int):
        self.gear = Gear(chainring, cog)

    def gear_inches(self):
        
        try:
            result = self.rear_wheel.wheel_diameter * self.gear.ratio()
        except TypeError:
            result = 0
        except AttributeError:
            result = 0
        
        return result


class Wheel:

    def __init__(self, rim_diameter: float, tire_height: float):
        self.rim_diameter = rim_diameter
        self.tire_hight = tire_height
        self.wheel_diameter = rim_diameter + (tire_height * 2)
        

class Gear:
    
    def __init__(self, chainring: int, cog: int):
        self.chainring = chainring
        self.cog = cog

    def ratio(self) -> float:
        
        try:
            ratio = round(self.chainring / self.cog, 2)
        except ZeroDivisionError:
            return 0
        else:
            return ratio
    

bike1 = Bicycle()
bike1.setup_gear(52, 11)
bike1.setup_wheel("r", 27, 0.5)

print(
    bike1.gear_inches()
)
