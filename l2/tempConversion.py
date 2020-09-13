class Temperature:

  def __init__(self, temp, unit):
    self.unit = "c" if (unit=="celsius" or unit=="c") else "f"
    self.temp = round(temp, 1)
  
  def convert(self):
    if (self.unit=="c"):
      return Temperature(1.8*self.temp+32, "f")
    else:
      return Temperature(5/9*(self.temp-32), "c")
  
  def __str__(self):
    return "%s %s" % (self.temp, self.unit)  


tempArr = [ Temperature(44, "f"), Temperature(2, "c"), Temperature(12, "f"),
            Temperature(24,"f"), Temperature(0,"celsius") ]

print("the array of temps:")
for x in tempArr:
  print(x)

print("temps converted:")
for x in tempArr:
  print(x.convert())
