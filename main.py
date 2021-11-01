while True: #sürekli çalışmasın


    exit = input("Type Y if you want to end the programme or N") 

    if(exit == "Y"):

        break

    elif(exit == "N"): #else

        Numberinserted = int(input("Please insert a number which consists of 2 digits:")) #camelCase

        def sayiAtama(Numberinserted):

            if ((Numberinserted >= 10) and (Numberinserted <= 99)):
                sayiOkunusu(Numberinserted)

                print("You entered valid answer.")

            else:
                print("You entered invalid answer.Please try again.")

        def sayiOkunusu(Numberinserted):

            number = Numberinserted #tek variable, silelim

            numList = [int(digit) for digit in str(number)]



            demet0 = {1: "on", 2: "yirmi", 3: "otuz", 4: "kırk", 5: "elli", 6: "altmış", 7: "yetmiş", 8: "seksen", 9: "doksan"}
            birler = demet0[numList[0]]


            demet1 = {1: "bir", 2: "iki", 3: "üç", 4: "dört", 5: "beş", 6: "altı", 7: "yedi", 8: "sekiz", 9: "dokuz"}
            onlar = demet1[numList[1]]
            #variable isimlerini düzeltelim
            print("{} {}".format(birler, onlar))

        sayiAtama(Numberinserted)
            #refactor yapalım

