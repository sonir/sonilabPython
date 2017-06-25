import deg

d = deg.get(0.0, 0.0, 0., 1.)
assert d == 0 , "deg0 ERROR"

d = deg.get(0.0, 0.0, 1., 1.)
assert d == 45 , "deg45 ERROR"

d = deg.get(0.0, 0.0, 1., 0.)
assert d == 90 , "deg90 ERROR"

d = deg.get(0.0, 0.0, 1., -1.)
assert d == 135 , "deg135 ERROR"

d = deg.get(0.0, 0.0, 0., -1.)
assert d == 180 , "deg180 ERROR"

d = deg.get(0.0, 0.0, -1., -1.)
assert d == 225 , "deg225 ERROR"

d = deg.get(0.0, 0.0, -1., 0.)
assert d == 270 , "deg270 ERROR"

d = deg.get(0.0, 0.0, 0., 0.)
assert d == 0 , "deg360 ERROR"


print("All tests are OK.")
