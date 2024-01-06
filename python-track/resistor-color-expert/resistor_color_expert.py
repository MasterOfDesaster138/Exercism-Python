resistors = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9,
}

tolerances = {
    "grey": 0.05, 
    "violet": 0.1,
    "blue": 0.25,
    "green": 0.5,
    "brown": 1,
    "red": 2,
    "gold": 5,
    "silver": 10
}

metric_prefix = {1000000000: "giga", 1000000: "mega", 1000: "kilo"}


def resistor_label(colors: list[str]):
    # Handle edge case
    if colors == ["black"]:
        return f"0 ohms"
    
    else:
        resistor_colors = colors[:-1]
        resistor = decode_resistor(resistor_colors)
        
        tolerance_colors = colors[-1]
        tolerance = decode_tolerance(tolerance_colors)
        
        return f"{resistor} {tolerance}"


def decode_tolerance(color: str) -> str:
    tolerance = tolerances[color]
    return f"±{tolerance}%"     


# Modified version of resistor_color_trio.py
def decode_resistor(colors: list[str]) -> str:
    color_values = [resistors[v] for v in colors]
    resistance = int(''.join(map(str, color_values[:-1])))
    magnitude = int(f"{resistance}{'0' * color_values[-1]}")
    suffix = "ohms"

    for base, prefix in metric_prefix.items():
        if magnitude >= base:
            suffix = f"{prefix}{suffix}"
            magnitude = float(magnitude / base)
            if magnitude.is_integer():
                magnitude = int(magnitude)
            break

    return f"{magnitude} {suffix}"
