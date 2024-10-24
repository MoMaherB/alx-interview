#!/usr/bin/python3
"""
A script: Reads standard input line by line and computes metrics
"""


def status_code(fileSize, statusCodes):
    """
    Prints generated status codt to standard output
    """
    print("File size: {}".format(fileSize))
    for key, value in sorted(statusCodes.items()):
        print("{}: {}".format(key, value))


stdin = __import__('sys').stdin
lineNumber = 0
fileSize = 0
statusCodes = {}
codes = ('200', '301', '400', '401', '403', '404', '405', '500')
try:
    for args in stdin:
        lineNumber += 1
        args = args.split()
        try:
            fileSize += int(args[-1])
            if args[-2] in codes:
                try:
                    statusCodes[args[-2]] += 1
                except KeyError:
                    statusCodes[args[-2]] = 1
        except (IndexError, ValueError):
            pass
        if lineNumber == 10:
            status_code(fileSize, statusCodes)
            lineNumber = 0
    status_code(fileSize, statusCodes)
except KeyboardInterrupt as e:
    status_code(fileSize, statusCodes)
    raise
