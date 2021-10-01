print("Selamlar, hoşgeldiniz.")

Numberinserted = int(input("Please insert a number which consists of 2 digits __"))


def sayiAtama(Numberinserted):
    if ((Numberinserted >= 10) and (Numberinserted <= 99)):
        sayiOkunusu(Numberinserted)
        print("You entered valid answer.")
    else:
        print("You entered invalid answer.Please try again.")

def sayiOkunusu(Numberinserted):

    demet = {11: "on bir", 12: "on iki", 13: "on üç", 14: "on dört", 15: "on beş"}
    print(demet[Numberinserted])


sayiAtama(Numberinserted)




