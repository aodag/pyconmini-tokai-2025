# importme2.py
import sys
print(__name__, "いるよ！" if "importme2" in sys.modules else "いないよ！")
import importme2
print(__name__, "いるよ！" if "importme2" in sys.modules else "いないよ！")

