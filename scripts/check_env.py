"""Sprawdza, czy środowisko Pythona ma zainstalowane wymagane biblioteki.

Uruchomienie (z katalogu głównego repozytorium):
    python scripts/check_env.py
"""

import importlib
import sys

REQUIRED = ["numpy", "matplotlib", "gymnasium"]


def main() -> int:
    print(f"Python {sys.version.split()[0]}")
    missing = []
    for name in REQUIRED:
        try:
            module = importlib.import_module(name)
            print(f"  OK   {name} {getattr(module, '__version__', '?')}")
        except ImportError:
            print(f"  BRAK {name}")
            missing.append(name)
    if missing:
        print("\nBrakujące pakiety. Zainstaluj je poleceniem:")
        print("    pip install -r requirements.txt")
        return 1
    print("\nŚrodowisko jest gotowe.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
