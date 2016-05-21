import dist

num = dist.run(0.,0.,1.,1.)
num = round(num,3)
assert num == 1.414

num = dist.run(-0.5,-0.5,.5,.5)
num = round(num,3)
assert num == 1.414

num = dist.run(0.0,0.0,0.4,0.4)
num = round(num,3)
assert num == 0.566
