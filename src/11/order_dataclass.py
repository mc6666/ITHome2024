from dataclasses import dataclass, field

# 指定樸克牌大小順序
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
SUITS = '♣ ♢ ♡ ♠'.split()
    
@dataclass(order=True)
class PlayingCard:
    sort_index: int = field(init=False, repr=False)
    rank: str
    suit: str

    # 計算排序索引值
    def __post_init__(self):
        self.sort_index = (RANKS.index(self.rank) * len(SUITS)
                           + SUITS.index(self.suit))        
        
if __name__ == '__main__':
    # 測試物件創建
    queen_of_hearts = PlayingCard('Q', '♡♠'[0]) # 單獨顯示紅心會出現亂碼
    ace_of_spades = PlayingCard('A', '♠')
    
    # 比較物件大小順序
    print(ace_of_spades > queen_of_hearts)
    
    