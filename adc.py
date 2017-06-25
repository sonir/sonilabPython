#!usr/bin/python

#SOURCE : https://learn.adafruit.com/raspberry-pi-analog-to-digital-converters/mcp3008

# ADC handler for mcp3008

### SPI CONNECTION ###
# VDD -> 3.3V
# VREF -> 3.3V
# AGND -> GND
# DGND -> GND
# CLK -> SCLK(23)
# DOUT -> MISO(21)
# DIN -> MOSI(19)
# CS / SHDN -> CE0(24)


import time
import spidev

spi = spidev.SpiDev()
spi.open(0,0)
# data = 0.0
# value = 0.0
# volts = 0.0
# temp = 0.0


def read(channel):
  adc = spi.xfer2([1,(8+channel)<<4,0])
  val = ((adc[1]&3) << 8) + adc[2]
  val = val/1023.0
  if val < 0.001:
    val = 0.0
  elif val > 0.997:
    val = 1.0
  return val


def release():
  spi.close()


