# heart(1 to 14), spade(1 to 14), diamond(1 to 14, club(1 to 14)
name = input("Your name: ")
n = int(input("How many cards do you want to dispense? "))
import itertools, random
deck = list(itertools.product(range(1,14),["spade","heart", "diamond", "club"]))
random.shuffle(deck)
print(name," got")
for i in range(n):
    print(deck[i][0], "of", deck[i][1])