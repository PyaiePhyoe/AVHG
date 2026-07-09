from engine import Engine
from diagnostics.diagnose import Diagnose

print("---------------")
print("AVHG Project - Phase 1")
print("---------------\n")
engine = Engine()
engine.start()
engine.show_info()
Diagnose(engine).start()
