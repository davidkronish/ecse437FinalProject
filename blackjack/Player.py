from chips import chips

class Player(object): 
    def __init__(self,name,chip_amt) -> None:
        self.name = name
        self.chips = chips(chip_amt)

    def __str__(self) -> str:
        return f"Player {self.name} has a total of {self.chips.total} chips."


    
