import sl_blink_pattern, sl_metro


blinker = sl_blink_pattern.SlBlinkPattern(100)
metro = sl_metro.Metro(1)

metro.set(blinker.bang())
count = 0
while True:
    if metro.update():
        print(blinker.update())
        count = count+1
        if count > 10:
            metro.set(blinker.bang())
            count = 0


# for var in range(30):
#     if metro.update():
#         print(blinker.update())
#
# metro.set(blinker.bang())
# for var in range(30):
#     if metro.update():
#         print(blinker.update())
#
# metro.set(blinker.bang())
# for var in range(30):
#     if metro.update():
#         print(blinker.update())
