"""
@Title of program: Tests.py
@Author: Chinmay Patil
@Date of creation: 2018-12-04 - 14:17
"""


import os
import time

#print(os.environ["Token"])

#os.environ["Token"] = "PLZ WORKS"

#print(os.environ["Token"])

fil = open("/datas/testing.txt","w")
fil.write("Test")
fil.close()

print(os.listdir("/datas"))

time.sleep(3600)