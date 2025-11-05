# importme3.py
import sys
sys.modules["ximportme3"] = sys.modules[__name__]
raise Exception()

