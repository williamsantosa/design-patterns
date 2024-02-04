import sys

# Declares factory method returning object of product class
class CarFactory:
  # Can create default implementation or leave blank
  def createCar(self, model):
    pass

# Concrete creators override factory method to change resulting product's type
class SedanCarFactory(CarFactory):
  def createCar(self, model):
    return SedanCar(model)

class HatchbackCarFactory(CarFactory):
  def createCar(self, model):
    return HatchbackCar(model)

# Object to be created
class Car:
  def __init__(self, model):
    self.model = model

  def carInformation(self):
    pass

# Extended cars
class SedanCar(Car):
  def __init__(self, model):
    self.model = model

  def carInformation(self):
    return f"Sedan with model: {self.model}"

class HatchbackCar(Car):
  def __init__(self, model):
    self.model = model

  def carInformation(self):
    return f"Hatchback with model: {self.model}"

# Application class deciding what to use
class Application:
  def initialize(self, carType):
    ret = None
    if carType.lower() == "sedan":
      ret = SedanCarFactory()
    elif carType.lower() == "hatchback":
      ret = HatchbackCarFactory()
    return ret

# Main (client)
if __name__=="__main__":
  factory = None
  while not factory:
    carType = input("Sedan or Hatchback: ")
    factory = Application().initialize(carType)
  model = ""
  while not model:
    model = input("Model: ")
  car = factory.createCar(model)
  print(car.carInformation())