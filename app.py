from math import pi


class Bicycle:
    
    def __init__(self, front_wheel, rear_wheel, gear):
        
        self.front_wheel = front_wheel
        self.rear_wheel = rear_wheel
        self.gear = gear

    def gear_inches(self):
        
        return round(
            self.rear_wheel.wheel_diameter * self.gear.ratio(),
            2
        )
    
    def circumference(self, wheel):
        return wheel.wheel_diameter * pi

    


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
    


bike1 = Bicycle(
    front_wheel=Wheel(27, 0.5),
    rear_wheel=Wheel(27, 0.7),
    gear=Gear(52, 11)
)

print(
    bike1.circumference(bike1.front_wheel)
)
