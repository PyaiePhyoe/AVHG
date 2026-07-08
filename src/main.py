from engine import Engine
from diagnostics.diagnose import Diagnose


print("AVHG Project - Phase 1")
print("---------------\n")
engine = Engine()
engine.start()
engine.show_info()
print("Systems")
print("---------------\n")
Diagnose(engine).start()
