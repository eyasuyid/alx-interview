#!/usr/bin/python3
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
    print("File size: {:d}".format(totalFileSize))
    for k, v in codes.items():
        if v != 0:
            print("{:s}: {:d}".format(k, v))


try:
    for line_text in sys.stdin:
        count += 1
        list_text = line_text.split(" ")
        if len(list_text) != 9:
            continue

        code = list_text[-2]
        fileSize = int(list_text[-1])
        totalFileSize += fileSize

        if count == 10:
            count = 0
            display()

        if code in codes.keys():
            codes[code] += 1
except Exception as e:
    pass
finally:
    display()