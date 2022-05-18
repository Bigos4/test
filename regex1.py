import re


def regex(txt):
    x = re.findall("\d", txt)

    if x:           # check if txt has any numbers
        y = ''
        for number in x:    # turn list to str
            y += number

        len_b = len(y)  # check the length before +1
        y = int(y) + 1
        len_a = len(str(y))  # check the length after +1

        len_diff = len_b - len_a  # difference

        zeros = ''
        while len_diff > 0:
            zeros += '0'
            len_diff -= 1

        letters = re.findall("\D", txt)
        word = ''
        for letter in letters:
            word += letter

        result = word + zeros + str(y)

    else:
        result = txt + '1'

    return result


text = "Gummy12"
print(regex(text))
