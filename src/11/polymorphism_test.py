# 載具
class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  # 載具方法
  def move(self):
    print("Move!")

# 轎車
class Car(Vehicle):
  pass

# 小艇
class Boat(Vehicle):
  def move(self):
    print("Sail!")

# 飛機
class Plane(Vehicle):
  def move(self):
    print("Fly!")

# 物件創建
car1 = Car("Ford", "Mustang")  
boat1 = Boat("Ibiza", "Touring 20") 
plane1 = Plane("Boeing", "747") 

# 執行物件方法 move
for x in (car1, boat1, plane1):
  print(x)
  x.move()