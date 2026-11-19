# Analects Book 15 (衛靈公). Same format as the pilot (drafts/analects-01/units.py): one unit per stretch
# between Zhu Xi's commentary interruptions (59 units, 41 passages; lemma 30 holds 15.18–19 and lemma 33
# holds 15.22–23, each with npas=2). Drafted in two parts: units_a.py (15.1–15.17, lemmata 0–29) and
# units_b.py (15.18–15.41, lemmata 30–58); this file joins them.
import importlib.util as _u, os as _os

def _load(name, var):
    p = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), name)
    s = _u.spec_from_file_location("analects15_" + var, p)
    m = _u.module_from_spec(s)
    s.loader.exec_module(m)
    return getattr(m, var)

UNITS = _load("units_a.py", "UNITS_A") + _load("units_b.py", "UNITS_B")
