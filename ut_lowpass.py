import lowpass

lowpass = lowpass.Lowpass(5)

def test_once () :
    global lowpass
    assert lowpass.run(1) == 0.2
    assert lowpass.run(1) == 0.4
    lowpass.run(1)
    lowpass.run(1)
    assert lowpass.run(1) == 1.0

test_once()
lowpass.print_all()
print "---"
lowpass.reset()
test_once()
lowpass.print_all()
print "---"
lowpass.reset()
lowpass.run(0.137)
lowpass.run(0.138)
lowpass.print_all()
print "---"

print "TEST OK."
