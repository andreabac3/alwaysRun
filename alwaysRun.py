#!/usr/bin/env python3

import sys
import subprocess
args= sys.argv[1:]
log = True
fileopen = None
f = None
try:
  while (True):
      pipes = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
      pipes.wait()
      #wait (thread primitive) the end of subprocess.
      std_out, std_err = pipes.communicate()
      if  pipes.returncode != 0 and log:
        #if log variable it's true and the subprocess has returned an error  you can append the std error to the log file.

        f = open("log.txt", "a")
        fileopen = True
        f.write(str(std_err.strip()))
        f.close()
        fileopen = False
except KeyboardInterrupt:
  print("\nYou have been kill the deamon \n")
  if fileopen and log:
    f.close






