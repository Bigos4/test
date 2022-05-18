import re


def increment_string(strng):
    ynum = re.search(r"\d+\Z", strng)
    if ynum:
        ynum = str(ynum.group())
        ylen = len(ynum)
        ynum = int(ynum) + 1
        ynum = str(ynum).zfill(ylen)
    else:
        ynum = "1"

    ystrng = re.search(r".*\D+", strng)
    if ystrng:
        ystrng = str(ystrng.group())
    else:
        ystrng = ""

    strng = ystrng + ynum

    return (strng)

# print("input string:")
# print(increment_string(input()))

tekst = "hfeiw329fhkja0009"
print(increment_string(tekst))