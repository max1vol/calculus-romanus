def to_roman(n):
    """Converts an integer to a Roman numeral."""
    if not 0 < n < 4000:
        raise ValueError(
            "Numerus debet esse inter I et MMMCMXCIX (Number must be between 1 and 3999)"
        )

    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    syb = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    roman_num = ""
    i = 0
    while n > 0:
        for _ in range(n // val[i]):
            roman_num += syb[i]
            n -= val[i]
        i += 1
    return roman_num


def from_roman(s):
    """Converts a Roman numeral to an integer."""
    roman_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0
    i = 0
    while i < len(s):
        if i + 1 < len(s) and roman_map[s[i]] < roman_map[s[i + 1]]:
            result += roman_map[s[i + 1]] - roman_map[s[i]]
            i += 2
        else:
            result += roman_map[s[i]]
            i += 1
    return result
