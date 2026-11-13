# rl-drone-control

Projekt z przedmiotu **Uczenie się ze wzmocnieniem** (Wydział Elektrotechniki i Informatyki, Politechnika Rzeszowska, rok akademicki 2026/2027).

## Opis projektu

Celem projektu jest samodzielne zaprojektowanie, zaimplementowanie i przeanalizowanie systemu wykorzystującego uczenie się ze wzmocnieniem do sterowania uproszczonym modelem drona w symulacji. Agent uczy się sterować ciągiem tak, aby osiągnąć i utrzymać zadaną wysokość przy ograniczeniach energii i zakłóceniach, a jego działanie jest porównywane z agentem bazowym.

## Uruchomienie

### 1. Przygotowanie środowiska (Python 3.12)

```
git clone https://github.com/Vvking321/rl-drone-control.git
cd rl-drone-control
python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # Linux / macOS
pip install -r requirements.txt
```

### 2. Sprawdzenie środowiska

```
python scripts/check_env.py
```

### 3. Uruchomienie projektu i eksperymentów

Skrypty środowiska, agentów i eksperymentów pojawią się w `src/` i `experiments/`. Ta sekcja zostanie jeszcze uzupełniona o polecenia odtwarzające wyniki zapisywane w `results/`.

## Sprawozdanie

Sprawozdanie znajduje się w katalogu `report/` (plik `raport.tex`). Kompilacja:

```
cd report
latexmk -pdf raport.tex
```

## Wsparcie AI

Korzystanie z narzędzi AI jest dokumentowane w pliku `docs/wsparcie_ai.md` oraz w sekcji „Wsparcie AI" sprawozdania.

## Autor

Patryk Dziki 179480
