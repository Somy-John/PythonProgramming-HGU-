s = float(input("Input your score : "))
t = input("Input Letter(L) or PF(PF) : ")

if t == "L" or t == "Letter" :
    if 90 <= s <= 100 :
        g = "A"
    elif 80 <= s < 90:
        g = "B"
    elif 70 <= s < 80:
        g = "C"
    elif 60 <= s < 70:
        g = "D"
    else:
        g = "F"
else:
    if 90 <= s <= 100 :
        g = "PD(Pass with Distinction)"
    elif 60 <= s < 90:
        g = "Pass"
    else:
        g = "F"

print(g)
