import accelerator as acc
import time

ACC_TAP_BANK = 3
ACC_TAPPED_STATE = 1
ACC_AXIS_MAX = 3
ACC_AXIS_MIN = 0


if __name__ == '__main__':

  try:

    while 1:
      if acc.tapDetection() == True:
        print 'detect your tap!'

      xyz = acc.measure()
      for i in range(ACC_AXIS_MIN, ACC_AXIS_MAX):
        print(xyz[i])

      time.sleep(0.1)

  except KeyboardInterrupt:
    pass

