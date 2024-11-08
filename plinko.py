import os
import random
import time
egyenleg = 100
jatek = input("Mit szeretnél játszan? (plinko)\n")
while jatek == "plinko" or ujra == "y":
    e_1 = "."

    k_1 = "."
    k_2 = "."

    h_1 = "."
    h_2 = "."
    h_3 = "."

    n_1 = "."
    n_2 = "."
    n_3 = "."
    n_4 = "."

    o_1 = "."
    o_2 = "."
    o_3 = "."
    o_4 = "."
    o_5 = "."
    os.system('cls')


    print(f"Egyenleg: {egyenleg}\n")

    print(f"    {e_1}\n   {k_1} {k_2}\n  {h_1} {h_2} {h_3}\n {n_1} {n_2} {n_3} {n_4}\n{o_1} {o_2} {o_3} {o_4} {o_5}\n3 2 1 2 3")

    rakas = int(input("\nMennyit szeretnél rakni? "))

    while rakas > egyenleg:
        print("Nem tudsz ennyit rakni.")
        rakas = int(input("Mennyit szeretnél rakni? "))

    egyenleg -= rakas

    os.system('cls')
    e_1 = "O"
    print(f"Egyenleg: {egyenleg}\n")
    print(f"    {e_1}\n   {k_1} {k_2}\n  {h_1} {h_2} {h_3}\n {n_1} {n_2} {n_3} {n_4}\n{o_1} {o_2} {o_3} {o_4} {o_5}\n3 2 1 2 3")
    time.sleep(1)

    if random.randint(1,2) == 1:
        k_1 = "O"
    else:
        k_2 = "O"

    os.system('cls')
    e_1 = "."
    print(f"Egyenleg: {egyenleg}\n")
    print(f"    {e_1}\n   {k_1} {k_2}\n  {h_1} {h_2} {h_3}\n {n_1} {n_2} {n_3} {n_4}\n{o_1} {o_2} {o_3} {o_4} {o_5}\n3 2 1 2 3")
    time.sleep(1)

    if k_1 == "O":
        if random.randint(1,2) == 1:
            h_1 = "O"
        else:
            h_2 = "O"
    else:
        if random.randint(1,2) == 1:
            h_2 = "O"
        else:
            h_3 = "O"

    os.system('cls')
    k_1 = "."
    k_2 = "."
    print(f"Egyenleg: {egyenleg}\n")
    print(f"    {e_1}\n   {k_1} {k_2}\n  {h_1} {h_2} {h_3}\n {n_1} {n_2} {n_3} {n_4}\n{o_1} {o_2} {o_3} {o_4} {o_5}\n3 2 1 2 3")
    time.sleep(1)

    if h_1 == "O":
        if random.randint(1,2) == 1:
            n_1 = "O"
        else:
            n_2 = "O"
    elif h_2 == "O":
        if random.randint(1,2) == 1:
            n_2 = "O"
        else:
            n_3 = "O"
    else:
        if random.randint(1,2) == 1:
            n_3 = "O"
        else:
            n_4 = "O"

    os.system('cls')
    h_1 = "."
    h_2 = "."
    h_3 = "."
    print(f"Egyenleg: {egyenleg}\n")
    print(f"    {e_1}\n   {k_1} {k_2}\n  {h_1} {h_2} {h_3}\n {n_1} {n_2} {n_3} {n_4}\n{o_1} {o_2} {o_3} {o_4} {o_5}\n3 2 1 2 3")
    time.sleep(1)

    if n_1 == "O":
        if random.randint(1,2) == 1:
            o_1 = "O"
        else:
            o_2 = "O"
    elif n_2 == "O":
        if random.randint(1,2) == 1:
            o_2 = "O"
        else:
            o_3 = "O"
    elif n_3 == "O":
        if random.randint(1,2) == 1:
            o_3 = "O"
        else:
            o_4 = "O"
    else:
        if random.randint(1,2) == 1:
            o_4 = "O"
        else:
            o_5 = "O"

    os.system('cls')
    n_1 = "."
    n_2 = "."
    n_3 = "."
    n_4 = "."
    print(f"Egyenleg: {egyenleg}\n")
    print(f"    {e_1}\n   {k_1} {k_2}\n  {h_1} {h_2} {h_3}\n {n_1} {n_2} {n_3} {n_4}\n{o_1} {o_2} {o_3} {o_4} {o_5}\n3 2 1 2 3")
    time.sleep(1)

    if o_1 == "O" or o_5 == "O":
        egyenleg += (rakas*3)
    elif o_2 == "O" or o_4 == "O":
        egyenleg += (rakas*2)
    else:
        egyenleg += (rakas*1) 
    
    ujra = input("Szeretnél még játszani?(y/n)\n")