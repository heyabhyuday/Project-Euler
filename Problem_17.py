#Problem 17: Numbers to Words
Ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
Tens = [["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"],
        ["Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]]
other = {0: "", 3: "Thousand", 6: "Million", 9: "Billion", 12: "Trillion"}


def triples(num):
    n3 = int(num[0])
    n2 = int(num[1])
    n1 = int(num[2])

    if n3 != 0:
        temp = Ones[int(n3)] + " Hundred "
    else:
        temp = ""
    if n2 == 1:
        temp = temp + Tens[0][n1]
    elif n2 == 0:
        temp = temp + Ones[n1]
    else:
        temp = temp + Tens[1][n2 - 2] + " " + Ones[n1]
    return temp.strip()

n = int(input().strip())
for a0 in range(n):
    num = input().strip()
    if int(num) != 0:
        l = len(num)
        if l % 3 == 2:
            num = "0" + num
        elif l % 3 == 1:
            num = "00" + num
        l = len(num)
        final = []
        for i in range(0, l, 3):
            number = triples(num[i:i + 3])
            temp = (number + " " + other[abs(i - l + 3)]).strip()
            if number != "":
                final.append(temp)
        print(" ".join(final))
    else:
        print("Zero")
