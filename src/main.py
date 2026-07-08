from engine import Engine
from systems.airsystem import AirSystem

print("AVHG Project - Phase 1")
print("---------------\n")
engine = Engine()
engine.show_info()
print("Systems")
print("---------------\n")
airSystem = AirSystem()
airSystem.diagnose_system()
