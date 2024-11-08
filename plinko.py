import os
import random
import time

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

egyenleg = 20
print(f"Egyenleg: {egyenleg}")

print(f"    {e_1}\n   {k_1} {k_2}\n  {h_1} {h_2} {h_3}\n {n_1} {n_2} {n_3} {n_4}\n{o_1} {o_2} {o_3} {o_4} {o_5}\n3 2 1 2 3")

rakas = int(input("\nMennyit szeretnél rakni? "))

while rakas > egyenleg:
    print("Nem tudsz ennyit rakni.")
    rakas = int(input("Mennyit szeretnél rakni? "))

egyenleg -= rakas

e = random.randint(1,1)
k = random.randint(1,2)
h = random.randint(1,4)
n = random.randint(1,6)
o = random.randint(1,9)
