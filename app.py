
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
    

input_data_examples = [
    {
       "chainring": 52,
        "cog": 11
    },
    {
       "chainring": 30,
        "cog": 27
    },
    {
       "chainring": 0,
        "cog": 15
    },
    {
       "chainring": 52,
        "cog": 0
    },
    {
       "chainring": 0,
        "cog": 0
    }
]

for data in input_data_examples:
    
    new_gear = Gear(**data)

    print(
        new_gear.ratio()
    )
