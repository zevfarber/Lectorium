# Analects Book 16 (季氏). Same format as the pilot (drafts/analects-01/units.py): one unit per stretch
# between Zhu Xi's commentary interruptions (35 units, 14 passages; the running head 論語巻八 that closes
# the lemma list is skipped by the build). Drafted in two parts: units_a.py (16.1, lemmata 0–12) and
# units_b.py (16.2–16.14, lemmata 13–34); this file joins them.
import importlib.util as _u, os as _os

def _load(name, var):
    p = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), name)
    s = _u.spec_from_file_location("analects16_" + var, p)
    m = _u.module_from_spec(s)
    s.loader.exec_module(m)
    return getattr(m, var)

UNITS = _load("units_a.py", "UNITS_A") + _load("units_b.py", "UNITS_B")
