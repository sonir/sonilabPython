import adc
import time

if __name__ == '__main__':
  try:

    while True:
      for i in range(0, 8):
        data = adc.readAdc(i)
        volts = adc.getVolts(i)
        temp = adc.getTemp(i)

        if i == 0 :
          print("adc  : {:8} ".format(data))
          print("volts: {:8.2f}".format(volts))
          print("temp : {:8.2f}".format(temp))

      time.sleep(0.5)

  except KeyboardInterrupt:
      adc.release()
