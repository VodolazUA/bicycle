
class Gear:
    
    @classmethod
    def ratio(cls, chainring: int, cog: int) -> float:
        
        try:
            ratio = round(chainring / cog, 2)
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
    ratio_res = Gear.ratio(**data)
    print(ratio_res)
