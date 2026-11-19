# Analects Book 13 (子路). Same format as the pilot (drafts/analects-01/units.py): one unit per stretch
# between Zhu Xi's commentary interruptions (52 units, 30 passages). Drafted in two halves:
# units_a.py (13.1–13.14, lemmata 0–24) and units_b.py (13.15–13.30, lemmata 25–51); this file joins them.
import importlib.util as _u, os as _os

def _load(name, var):
    p = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), name)
    s = _u.spec_from_file_location("analects13_" + var, p)
    m = _u.module_from_spec(s)
    s.loader.exec_module(m)
    return getattr(m, var)

UNITS = _load("units_a.py", "UNITS_A") + _load("units_b.py", "UNITS_B")
