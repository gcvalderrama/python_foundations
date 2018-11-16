
def getHundred(y):
    sb = ""
    units = ["", "One ", "Two ", "Three ", "Four ", "Five ", "Six ", "Seven ", "Eight ", "Nine ", "Ten ", "Eleven "
        , "Twelve ", "Thirteen ", "Fourteen ", "Fifteen ", "Sixteen ", "Seventeen ", "Eighteen ", "Nineteen "]
    tens = ["", "", "Twenty ", "Thirty ", "Forty ", "Fifty ", "Sixty ", "Seventy ", "Eighty ", "Ninety "]
    if y % 100 < 20:
        sb += units[y % 100]
        y = y // 100
    else:
        sb += units[y % 10]
        y = y // 10
        sb = tens[y % 10] + sb
        y = y // 10

    if y > 0:
        sb = "Hundred " + sb
        sb = units[y] + sb

    return sb


def numberToWords(num):
    if not num :
        return "Zero"
    nearest = ["", "", "", "Thousand ", "", "", "Million ", "", "", "Billion "]
    i = 0
    n = num
    sb = ""
    while n > 0:
        y = n % 1000
        n = n // 1000
        if y > 0:
            sb = nearest[i] + sb
            sb = getHundred(y) + sb
        i += 3

    return sb


if __name__ == '__main__':
    print(numberToWords(12345))
