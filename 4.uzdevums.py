skaitlis = int(input("Ievadiet veselu nenegatīvu skaitli: "))
if skaitlis < 0:
    print("Faktoriālu nevar aprēķināt negatīvam skaitlim.")
elif skaitlis == 0:
    faktoriāls = 1
else:
    faktoriāls = 1
    for i in range(1, skaitlis + 1):
        faktoriāls *= i
