# Invert degree 180.
# Ex. 270 -> 90

import deg_inv

print deg_inv.get(359)

assert deg_inv.get(0)==180 , "deg 0 ERR"
assert deg_inv.get(90)==270 , "deg 90 ERR"
assert deg_inv.get(180)==0 , "deg 180 ERR"
assert deg_inv.get(270)==90 , "deg 270 ERR"

assert deg_inv.get(45)==225 , "deg 45 ERR"
assert deg_inv.get(360)==180 , "deg 360 ERR"
assert deg_inv.get(135)==315 , "deg 360 ERR"
assert deg_inv.get(315)==135 , "deg 315 ERR"
assert deg_inv.get(359)==179 , "deg 359 ERR"
assert deg_inv.get(227)==47 , "deg 227 ERR"
# assert deg_inv.get(315)==135 , "deg 315 ERR"
print ("deg_inv test is OK")
