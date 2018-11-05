#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess
from sys import argv

args= argv[1:]
log = True
filelog = None
stillActive, is_open = False, False #do not touch these variables
try:
  while True:
      pipes = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
      stillActive = True
      print("The current pid of subprocess: ", pipes.pid)
      pipes.wait()
      stillActive = False
      #wait (thread primitive) the end of subprocess.
      print(pipes.pid)
      std_out, std_err = pipes.communicate()
      if  pipes.returncode != 0 and log:
        #if log variable it's true and the subprocess has returned an error  you can append the std error to the log file.

        filelog = open("log.txt", "a")
        is_open = True
        filelog.write(str(std_err.strip()))
        filelog.close()
        is_open = False
except KeyboardInterrupt:
  print("\nYou have killed the Demon \n")
  if is_open and log: filelog.close
  if stillActive:
    pipes.terminate()
    print("The subprocess has been killed\n")
