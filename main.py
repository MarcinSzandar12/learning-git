print("Zadanie 1")

print("Lista zakupów")

shopping_list = {"piekarnia":["chleb", "bułki", "pączek"], "warzywniak":["marchew", "seler", "rukola"]}

for x, y in shopping_list.items():
    print("Idę do", x,"kupuję tu następujące rzeczy:", y)

print("W sumie kupuję", len(shopping_list["piekarnia"]) + len(shopping_list["warzywniak"]), "produktów.")


print("\nZadanie 2")

for i in range(0, 100):
    if i % 5 == 0:
        print(i)
        power = i * i * i
        print(power)