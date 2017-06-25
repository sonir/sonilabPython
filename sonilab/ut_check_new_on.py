import check_new_on

assert check_new_on.run(0.0) == False
assert check_new_on.run(0.1) == True
assert check_new_on.run(0.1) == False
assert check_new_on.run(1.1) == False
# reset
assert check_new_on.run(0.0) == False
# recovery
print "RCV"
assert check_new_on.run(0.5) == True
assert check_new_on.run(1) == False
assert check_new_on.run(0.0) == False
assert check_new_on.run(0.2) == True

print "all OK"
