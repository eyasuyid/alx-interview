#!/usr/bin/python3
"""Module for manuplating stdout log"""

import sys

codes = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0
        }
totalFileSize = 0
count = 0


def display():
    """Fucntion display the result"""

    print("File size: {:d}".format(totalFileSize))
    for k, v in sorted(codes.items()):
        if v != 0:
            print("{:s}: {:d}".format(k, v))


try:
    for line_text in sys.stdin:
        list_text = line_text.split(" ")
        if len(list_text) != 9:
            continue
        code = list_text[-2]
        fileSize = int(list_text[-1])
        totalFileSize += fileSize
        if code in codes.keys():
            codes[code] += 1
            count += 1
        if count == 10:
            count = 0
            display()
except Exception as e:
    pass
finally:
    display()
