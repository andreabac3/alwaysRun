#!/usr/bin/env python3

import sys
import subprocess
args= sys.argv[1:]
log = True
is_open, filelog = None, None
try:
  while True:
      pipes = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
      pipes.wait()
      #wait (thread primitive) the end of subprocess.
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
  if is_open and log:
    filelog.close
