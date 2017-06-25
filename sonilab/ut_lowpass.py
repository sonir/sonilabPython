import lowpass

lowpass = lowpass.Lowpass(5)

assert lowpass.run(1) == 0.2
assert lowpass.run(1) == 0.4
lowpass.run(1)
lowpass.run(1)
assert lowpass.run(1) == 1.0
print "TEST OK."
