# Analects Book 14 (憲問). Same format as the pilot (drafts/analects-01/units.py): one unit per stretch
# between Zhu Xi's commentary interruptions (75 units, 47 passages). Drafted in three parts:
# units_a.py (14.1–14.17, lemmata 0–22), units_b.py (14.18–14.33, lemmata 23–48) and units_c.py
# (14.34–14.47, lemmata 49–74); this file joins them.
import importlib.util as _u, os as _os

def _load(name, var):
    p = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), name)
    s = _u.spec_from_file_location("analects14_" + var, p)
    m = _u.module_from_spec(s)
    s.loader.exec_module(m)
    return getattr(m, var)

UNITS = _load("units_a.py", "UNITS_A") + _load("units_b.py", "UNITS_B") + _load("units_c.py", "UNITS_C")
