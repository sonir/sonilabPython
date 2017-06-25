""" This is simple module for finding first on by value. """

# init val for previous bal
prev = 0.0

def run (val):
  global prev

  if val > 0.0 and prev == 0.0:
    prev = val
    return True
  elif val == 0.0:
    reset()
    return False
  else:
    return False

def reset():
  global prev
  prev = 0.0

