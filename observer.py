class Observer:
    def __init__(self):
        pass

    def callback(self, adr, val1, val2):
        print("got callback")
        print(adr)
        print(val1)
        print(val2)
