from dataclasses import dataclass
from typing import List
from enum import Enum, auto

class Position(Enum):
    FRONT_LEFT = auto()
    FRONT_RIGHT = auto()
    BACK_LEFT = auto()
    BACK_RIGHT = auto()

# 輪胎
@dataclass
class Wheel:
    position:Position # 安裝位置
    brand:str    # 廠牌
    
# 轎車
@dataclass
class Car(): # 轎車
    type:str  # 轎車類別
    power:int # 馬力
    size:int     # 輪胎尺寸
    wheels: List[Wheel] # 輪胎
        
if __name__ == '__main__':
    # 測試物件創建
    car1 = Car(type='type_a', power=2000, size=215, wheels=[
                Wheel(position=Position.FRONT_LEFT, brand='米其林'),
                Wheel(position=Position.FRONT_RIGHT, brand='普利司通'),
                Wheel(position=Position.BACK_LEFT, brand='米其林'),
                Wheel(position=Position.BACK_RIGHT, brand='普利司通')
                ])
    
    # 顯示物件
    print(car1)
    
    