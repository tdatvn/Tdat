a = 2
playerscore = 0
computerscore = 0

while a > 1:
    #Ti so
    print("Ti So: Player",playerscore,"-",computerscore,"Computer")

    #Nhap thu vien
    import random
    import os
    import time

    #Clear Screen
    os.system('cls')
    print("Ti So: Player",playerscore,"-",computerscore,"Computer")
    print("─────────────────────────────")

    #Gioi thieu
    print("[1]Keo     [2]Bua     [3]Bao")

    #Ngan cach
    print("─────────────────────────────")

    #Tao bien
    computer = random.randint(1,3)
    player = input("Ban chon: ")

    #Lenh chuyen doi
    if player == "1":
        os.system('cls')
        print("Ti So: Player",playerscore,"-",computerscore,"Computer")
        print("─────────────────────────────")
        print("[1]Keo     [2]Bua     [3]Bao")
        print("─────────────────────────────")
        print("Ban chon: Keo")
        player = "Keo"
    elif player == "2":
        os.system('cls')
        print("Ti So: Player",playerscore,"-",computerscore,"Computer")
        print("─────────────────────────────")
        print("[1]Keo     [2]Bua     [3]Bao")
        print("─────────────────────────────")
        print("Ban chon: Bua")
        player = "Bua"
    elif player == "3":
        os.system('cls')
        print("Ti So: Player",playerscore,"-",computerscore,"Computer")
        print("─────────────────────────────")
        print("[1]Keo     [2]Bua     [3]Bao")
        print("─────────────────────────────")
        print("Ban chon: Bao")
        player = "Bao"

    #Chuyen doi "number" sang "text"
    if computer == 1:
        computer = "Keo"
    elif computer == 2:
        computer = "Bua"
    elif computer == 3:
        computer = "Bao"

    #In bien Computer ra man hinh
    if player == "1":
        print("May chon: ",computer)
    elif player == "2":
        print("May chon: ",computer)
    elif player == "3":
        print("May chon: ",computer)
    elif player == "Keo":
        print("May chon: ",computer)
    elif player == "Bua":
        print("May chon: ",computer)
    elif player == "Bao":
        print("May chon: ",computer)

    #Lenh
    if player == computer:
        print("Draw!")
        Score = "Draw!"
    elif player == "Keo":
        if computer == "Bua":
            Score = "You Lose!"
            print(Score)
        elif computer == "Bao":
            Score = "You Win!"
            print(Score)
    elif player == "Bua":
        if computer == "Keo":
            Score = "You Win!"
            print(Score)
        elif computer == "Bao":
            Score = "You Lose!"
            print(Score)
    elif player == "Bao":
        if computer == "Bua":
            Score = "You Win!"
            print(Score)
        elif computer == "Keo":
            Score = "You Lose!"
            print(Score)

    #Lenh ti so
    if Score == "You Win!":
        playerscore = playerscore + 1
    elif Score == "You Lose!":
        computerscore = computerscore + 1
    elif Score == "Draw!":
        playerscore = playerscore + 1
        computerscore = computerscore + 1

    #Ngan cach
    print("─────────────────────────────")
    time.sleep(3)
