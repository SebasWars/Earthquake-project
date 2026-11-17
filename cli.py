from src.quakes.filters import filter_quakes
from src.quakes.loader import load_quake

from src.quakes.stats import strongest_quake, average_depth, quakes_per_day, dayly_sumary

quakes = load_quake()

""" stronger_than_5 = filter_quakes(quakes, min_mag=5)
recent = filter_quakes(quakes, start="2026-11-14", end="2026-11-17")
both = filter_quakes(quakes, min_mag=5, start="2026-11-14", end="2026-11-17") """


strongest = strongest_quake(quakes)
print(strongest)