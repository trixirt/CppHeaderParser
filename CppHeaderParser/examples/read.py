#!/usr/bin/python3
#
# call with
# ./read.py <file>
#
# Look for errors.

import sys
sys.path = ["../"] + sys.path
import CppHeaderParser
try:
    cppHeader = CppHeaderParser.CppHeader(sys.argv[1])
except CppHeaderParser.CppParseError as e:
    print(e)
    sys.exit(1)
