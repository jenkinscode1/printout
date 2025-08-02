# jprint/__init__.py
import os
import sys

def printout(*args, logfile=None, **kwargs):
    """
    Works like print, but also logs to a file.
    If logfile is None, defaults to <script_name>_log.log.
    """
    # Determine default log file
    if logfile is None:
        script_name = os.path.splitext(os.path.basename(sys.argv[0]))[0]
        logfile = f"{script_name}_log.log"

    # Join args into a message
    message = " ".join(str(arg) for arg in args)

    # Print to console
    print(message, **kwargs)

    # Append to log file
    with open(logfile, "a", encoding="utf-8") as f:
        f.write(message + "\n")