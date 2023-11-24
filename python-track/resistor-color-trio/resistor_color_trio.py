"""
The program will take 3 colors as input, and outputs the correct value, in ohms.
The color bands are encoded as follows:

- Black: 0
- Brown: 1
- Red: 2
- Orange: 3
- Yellow: 4
- Green: 5
- Blue: 6
- Violet: 7
- Grey: 8
- White: 9

In Resistor Color Duo you decoded the first two colors.
For instance: orange-orange got the main value `33`.
The third color stands for how many zeros need to be added to the main value.
The main value plus the zeros gives us a value in ohms.
For the exercise it doesn't matter what ohms really are.
For example:

- orange-orange-black would be 33 and no zeros, which becomes 33 ohms.
- orange-orange-red would be 33 and 2 zeros, which becomes 3300 ohms.
- orange-orange-orange would be 33 and 3 zeros, which becomes 33000 ohms.

(If Math is your thing, you may want to think of the zeros as exponents of 10.
If Math is not your thing, go with the zeros.
It really is the same thing, just in plain English instead of Math lingo.)

This exercise is about translating the colors into a label:

> "... ohms"

So an input of `"orange", "orange", "black"` should return:

> "33 ohms"

When we get to larger resistors, a [metric prefix][metric-prefix] is used to indicate a larger magnitude of ohms, such as "kiloohms".
That is similar to saying "2 kilometers" instead of "2000 meters", or "2 kilograms" for "2000 grams".

For example, an input of `"orange", "orange", "orange"` should return:

> "33 kiloohms"
"""

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

metric_prefix = {1000000000: "giga", 1000000: "mega", 1000: "kilo"}


def label(colors):
    res = [resistors[v] for v in colors]
    resistance = int(f"{res[0]}{res[1]}")
    magnitude = int(f"{resistance}{'0'*res[2]}")
    suffix = "ohms"

    for base, prefix in metric_prefix.items():
        if magnitude >= base:
            suffix = f"{prefix}{suffix}"
            magnitude = int(magnitude / base)
            break

    return f"{magnitude} {suffix}"