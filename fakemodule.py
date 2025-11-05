import sys

sys.modules["fake"] = "this is fake module"
import fake
fake == "this is fake module"
