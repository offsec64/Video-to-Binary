#!/usr/bin/env python
import base64
import time

t= "".encode("ascii")
print("".join(["{:08b}".format(x) for x in t]))


time.sleep(2)