# Analects Book 8 (泰伯). Same format as the pilot (drafts/analects-01/units.py): one unit per stretch
# between Zhu Xi's commentary interruptions (33 units, 21 passages). Drafted in two halves:
# units_a.py (8.1–8.10, lemmata 0–15) and units_b.py (8.11–8.21, lemmata 16–32); this file joins them.
import importlib.util as _u, os as _os

def _load(name, var):
    p = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), name)
    s = _u.spec_from_file_location("analects08_" + var, p)
    m = _u.module_from_spec(s)
    s.loader.exec_module(m)
    return getattr(m, var)

UNITS = _load("units_a.py", "UNITS_A") + _load("units_b.py", "UNITS_B")
