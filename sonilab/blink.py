def run(val):
    if val == 1 or val == 0:
        return ( (val - 1)*(-1) )
    else:
        raise ValueError("Must the param 1 or 0")
