#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from subprocess import PIPE, Popen
from sys import argv

try:
    if len(argv) < 2:
        raise Exception
except Exception:
    print("Missing Args, please see the documentation at:\nhttps://github.com/andreabac3/alwaysRun \n")
    exit(1)
args = argv[1:]
log = True
pipes = None
stillActive, is_open = False, False  # do not touch these variables
try:
    while True:
        pipes = Popen(args, stdout=PIPE, stderr=PIPE)
        stillActive = True
        print("The current pid of subprocess: ", pipes.pid)
        pipes.wait()
        stillActive = False
        # wait (thread primitive) the end of subprocess.
        std_out, std_err = pipes.communicate()
        if pipes.returncode != 0 and log:
            # if log variable it's true and the subprocess has returned an error  you can append the std error to the log file.
            with open("log.txt", "a") as filelog:
                filelog.write(str(std_err.strip()))
except KeyboardInterrupt:
    print("\nYou have killed the Demon \n")
    if stillActive and pipes is not None:
        pipes.terminate()
        print("The subprocess has been killed\n")
    exit(0)
