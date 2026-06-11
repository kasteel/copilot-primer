from __future__ import annotations

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from app.db.bootstrap import bootstrap_database


if __name__ == "__main__":
    path = bootstrap_database()
    print(f"Bootstrapped database at {path}")
