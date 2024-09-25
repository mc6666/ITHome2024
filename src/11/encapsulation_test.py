from dataclasses import dataclass, field

# 轎車
@dataclass
class Car(): # 轎車
    type:str  # 轎車類別
    power:int # 馬力
    size:int  # 輪胎尺寸
    _year:int = field(init=False, repr=False) # 出廠年度

    def set_year(self, year):
        self._year = year
        
if __name__ == '__main__':
    # 測試物件創建
    car1 = Car('type_a', 2000, 215)
    car1.set_year(2020)
    
    # 顯示物件
    print(car1)
    print(car1._year > 2022)
    
    
    