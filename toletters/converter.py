__units = ["", "un", "deux", "trois", "quatre", "cinq", "six", "sept", "huit", "neuf", "dix", "onze", "douze", "treize",
           "quatorze", "quinze", "seize", "dix-sept", "dix-huit", "dix-neuf"]
__tens = ["", "dix", "vingt", "trente", "quarante", "cinquante", "soixante", "soixante", "quatre-vingt",
          "quatre-vingt"]
__suffix = ["", "mille", "million", "milliard", "billion", "billiard", "trillion", "trilliard"]


def __convertHundreds(num, suffix):
    str_units, str_tens, str_hundred = "", "", ""
    units = num % 10
    tens = (num % 100) - units
    hundreds = (num % 1000) - (tens + units)
    hundreds, tens, units = hundreds // 100, tens // 10, int(units)
    if num == 0:
        return "zero" if suffix == "" else ""
    elif num == 1:
        return "un" if suffix == "" else ("un " + suffix if suffix != "mille" else "mille")
    else:
        str_units = __units[units]
        if tens == 1 and units > 0:
            str_tens = __units[10 + units]
            str_units = ""
        elif tens == 7 or tens == 9:
            str_units = ""
            str_tens = __tens[tens] + " " + __units[10 + units]
        else:
            str_tens = __tens[tens]
        str_tens += "s" if units == 0 and tens == 8 else ""
        str_hundred = (__units[hundreds] if hundreds > 1 else "") + (" cent" if hundreds > 0 else "") + (
            "s" if hundreds > 1 and tens == 0 else "")

    return (str_hundred + " " if str_hundred != "" else "") + (str_tens + " " if str_tens != "" else "") + (
        str_units + " " if str_units != "" else "") + suffix


def toLetters(num: int | str, sep=" "):
    if isinstance(num, int) or (isinstance(num, str) and num.isdigit()):
        num = str(num)
    else:
        raise TypeError("number must be int or string of digits")

    num = num.strip().lstrip('0')
    if len(num) > len(__suffix) * 3:
        raise ValueError("nombre trop long")
    num = num[::-1]
    numArr = []
    for i in range(0, len(num), 3):
        numArr.append(num[i:i + 3][::-1])
    numArr = [int(x) for x in numArr if x != '']
    return (" ".join([
                         __convertHundreds(x, __suffix[i]).strip()
                         for i, x in enumerate(numArr)][::-1])
            .replace(" ", sep))
