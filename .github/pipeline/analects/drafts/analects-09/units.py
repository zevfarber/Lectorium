# Analects Book 9 (子罕). Same format as the pilot (drafts/analects-01/units.py): one unit per stretch
# between Zhu Xi's commentary interruptions (45 units, 30 passages). Drafted in two halves:
# units_a.py (9.1–9.11, lemmata 0–21) and units_b.py (9.12–9.30, lemmata 22–44); this file joins them.
import importlib.util as _u, os as _os

def _load(name, var):
    p = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), name)
    s = _u.spec_from_file_location("analects09_" + var, p)
    m = _u.module_from_spec(s)
    s.loader.exec_module(m)
    return getattr(m, var)

UNITS = _load("units_a.py", "UNITS_A") + _load("units_b.py", "UNITS_B")
