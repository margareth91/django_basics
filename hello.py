
print('Hello Django Girls!')

if 3 > 2:
    print("To dziala!")
else:
    print("5 nie jest wieksze od 2")

name = "dziosia"
if name == "dziusio":
    print("czesc dziusio")
elif name == "dziosia":
    print("czesc dziosia")
else:
    print("czesc galu anonimie")


def hi():
    print("hej!")
    print("jak sie masz?")


hi()


def hi_2(imie):
    if name == "dziusio":
        print("czesc dziusio")
    elif name == "dziosia":
        print("czesc dziosia")
    else:
        print("czesc galu anonimie")


hi_2("fiodus")


girls = ["Monica", "Rachel", "Phoebe", "Dziosia"]


def hi_3(name):
    print(f"Witaj {name}! :)")


for name in girls:
    hi_3(name)
    print("Kolejna dziewczyna")


for i in range(1, 10):
    print(i)