from enum import Enum

class PlayerSymbol(Enum):
    PLAYER_1 = "\u25ce"
    PLAYER_2 = "\u25c9"
    
print(PlayerSymbol.PLAYER_1.value)
print(PlayerSymbol.PLAYER_2.value)    



