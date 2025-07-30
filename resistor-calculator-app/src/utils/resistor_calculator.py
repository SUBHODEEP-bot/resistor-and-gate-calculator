def calculate_resistor_value(band1, band2, multiplier, tolerance):
    color_codes = {
        'black': 0,
        'brown': 1,
        'red': 2,
        'orange': 3,
        'yellow': 4,
        'green': 5,
        'blue': 6,
        'violet': 7,
        'gray': 8,
        'white': 9,
    }

    multiplier_codes = {
        'black': 1,
        'brown': 10,
        'red': 100,
        'orange': 1000,
        'yellow': 10000,
        'green': 100000,
        'blue': 1000000,
        'gold': 0.1,
        'silver': 0.01,
    }

    tolerance_codes = {
        'brown': '±1%',
        'red': '±2%',
        'green': '±0.5%',
        'blue': '±0.25%',
        'violet': '±0.1%',
        'gray': '±0.05%',
        'gold': '±5%',
        'silver': '±10%',
        'none': '±20%',
    }

    if band1 not in color_codes or band2 not in color_codes or multiplier not in multiplier_codes:
        return "Invalid color selection"

    resistance_value = (color_codes[band1] * 10 + color_codes[band2]) * multiplier_codes[multiplier]
    tolerance_value = tolerance_codes.get(tolerance, 'Invalid tolerance selection')

    return f"Resistance: {resistance_value} Ohms, Tolerance: {tolerance_value}"