
class Bicycle:
    
    def __init__(self):
        self.front_wheel = None
        self.rear_wheel = None
        self.gear = None
    
    def setup_wheels(self, front_wheel=None, rear_wheel=None):
        
        if front_wheel is not None:
            self.front_wheel = front_wheel
        
        if rear_wheel is not None:
            self.rear_wheel = rear_wheel
            
    def setup_gear(self, chainring: int, cog: int):
        self.gear = Gear(chainring, cog)

    def gear_inches(self):
        
        try:
            result = round(self.rear_wheel.wheel_diameter * self.gear.ratio(), 2)
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
bike1.setup_wheels(rear_wheel=Wheel(27, 0.7)) # лише заднє колесо
# bike1.setup_wheels(Wheel(27, 0.5), Wheel(27, 0.7)) # два колеса

print(
    bike1.gear_inches()
)
