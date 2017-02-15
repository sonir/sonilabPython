import posi
import math

# x, y = posi.get(180)
# print("{0},{1}".format(x,y))


x, y = posi.get(0)
assert x==0.0 and y==1.0

# x, y = posi.get(45)
# print("{0},{1}".format(x,y))
# assert x==1.0 and y==1.0

x, y = posi.get(90)
assert x==1.0 and y==0.0

# x, y = posi.get(135)
# assert x==1.0 and y==-1.0

x, y = posi.get(180)
assert x==0.0 and y==-1.0

# x, y = posi.get(225)
# assert x==-1.0 and y==-1.0

x, y = posi.get(270)
assert x==-1.0 and y==0.0

# x, y = posi.get(315)
# assert x==-1.0 and y==1.0

x, y = posi.get(360)
assert x==-0.0 and y==1.0
