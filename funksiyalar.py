def calculyator(son1, son2, belgi):
    if belgi == "+":
        return f"Yig'indi: {son1 + son2}"
    elif belgi == "-":
        return f"Ayirma: {son1 - son2}"
    elif belgi == "*":
        return f"Ko'paytma: {son1 * son2}"
    elif belgi == "/":
        return f"Bo'linma: {son1 / son2}"
    else:
        print(f"Qiymat xato kiritildi!")

son1 = int(input("Birinchi sonni kiriting: "))
son2 = int(input("Ikkinchi sonni kiriting: "))
belgi = input("Belgini kiriting(+, -, *, /): ")

print(calculyator(son1, son2, belgi))