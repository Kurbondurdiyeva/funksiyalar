# 1 - masala
def salomlash(ism):
    return f"Assalomu alaykum {ism}!"

print(salomlash("Zuhra"))


# 2 - masala
def katta_kichik(son1, son2):
    if son1 > son2:
        return f"Katta son {son1}"
    elif son2 > son1:
        return f"Katta son {son2}"
    else:
        return f"{son1} = {son2} - Bu sonlar teng!"

son1 = int(input("Birinchi sonni kiriting: "))
son2 = int(input("Ikkinchi sonni kiriting: "))

print(katta_kichik(son1, son2))
