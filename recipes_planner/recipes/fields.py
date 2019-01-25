# Constants for all available difficulty types.
SIMPLE = 1
MEDIUM = 2
DIFFICULT = 3

# Names for all available difficulty types.
DIFFICULTIES = (
    (SIMPLE, "simple"),
    (MEDIUM, "medium"),
    (DIFFICULT, "difficult"),
)

# Unit names ised from:
# https://github.com/hgrecco/pint/blob/master/pint/default_en.txt


GENERIC_UNIT_NAMES = [
    "whole",       # a whole "something"
    "taste",       # add ingredient as needed
]

VOLUME_UNIT_NAMES = [
    # -- Volume
    "liter",       # 1e-3 * m ** 3 = l = L = litre
    "cc",          # centimeter ** 3 = cubic_centimeter

    # -- USCSDryVolume
    "dry_pint",    # 33.6003125 cubic_inch  = dpi = US_dry_pint
    # "dry_quart",   # 2 dry_pint = dqt = US_dry_quart
    # "dry_gallon",  # 8 dry_pint = dgal = US_dry_gallon
    # "peck",        # 16 dry_pint = pk
    "bushel",      # 64 dry_pint = bu
    # "dry_barrel",  # 7065 cubic_inch = US_dry_barrel

    # -- USCSLiquidVolume
    # "minim",       # liquid_pint / 7680
    # "fluid_dram",  # liquid_pint / 128 = fldr = fluidram = US_fluid_dram
    "fluid_ounce", # liquid_pint / 16 = floz = US_fluid_ounce = US_liquid_ounce
    # "gill",        # liquid_pint / 4 = gi = liquid_gill = US_liquid_gill
    "pint",        # 28.875 cubic_inch = pt = liquid_pint = US_pint
    # "quart",       # 2 liquid_pint = qt = liquid_quart = US_liquid_quart
    # "gallon",      # 8 liquid_pint = gal = liquid_gallon = US_liquid_gallon

    # -- USCSVolumeOther
    "teaspoon",    # tablespoon / 3 = tsp
    "tablespoon",  # floz / 2 = tbsp = Tbsp = Tblsp = tblsp = tbs = Tbl
    "shot",        # 3 * tablespoon = jig = US_shot
    "cup",         # 8 fluid_ounce = cp = liquid_cup = US_liquid_cup
    # "barrel",      # 31.5 * gallon = bbl
    # "oil_barrel",  # 42 * gallon = oil_bbl
    # "beer_barrel", # 31 * gallon = beer_bbl
    # "hogshead",    # 63 * gallon
]

# Combine all the unit names here
UNIT_NAMES = GENERIC_UNIT_NAMES + VOLUME_UNIT_NAMES
UNITS = list(zip(range(len(UNIT_NAMES)), UNIT_NAMES))