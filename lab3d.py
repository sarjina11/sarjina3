#!/usr/bin/env python3

# Author ID: skarki28

import subprocess

def free_space():
    # Execute the command and get the output
    result = subprocess.run("df -h | grep '/$' | awk '{print $4}'", shell=True, capture_output=True, text=True)
    # Return the free space as a UTF-8 string with stripped newline
    return result.stdout.strip()

if __name__ == '__main__':
    print(free_space())

