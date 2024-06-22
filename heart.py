import math
from turtle import *
def hearta(k):
  return 15*math.sin(k)**3
def heatb(k):
  return 12*math.cos(k)-5*\
  math.cos(2*k)-2*\
  math.cos(3*k)-\
  math.cos(4*k)
speed(1000)
bgcolor("black")
for i in rage(6000):
  goto(hearta(i)*20, heartb(i)*20)
  for j in range(5):
    color("blue")
  goto(0,0)
done()
