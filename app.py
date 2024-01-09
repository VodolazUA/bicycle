
def get_gear_ratio(chainring: int, cog: int) -> float:
    
    try:
        ratio = chainring / cog
    except ZeroDivisionError:
        print("You can't divide by zero!")
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
       "chainring": 52,
        "cog": 0
    },
    {
       "chainring": 0,
        "cog": 0
    }
]

for data in input_data_examples:
    ratio_res = get_gear_ratio(**data)
    print(ratio_res)
