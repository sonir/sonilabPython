import os, sys
# sys.path.append('./sonilab') # set search path
import sh


def run():
  pid = os.getpid()
  sh.run("kill "+str(pid))
