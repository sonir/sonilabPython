import subprocess

def run():
  cmd = "sudo halt"
  subprocess.call( cmd, shell=True  )
