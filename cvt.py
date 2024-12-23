values = "AKQJT98765432"
shapes = "schd"


def int2card(i):
    card = values[i // 4]
    card += shapes[i % 4]
    return card


def card2int(card):
    i = values.find(card[0]) * 4
    i += shapes.find(card[1])
    return i


# import random

# cards = [0 for _ in range(52)]
# for i in range(1_000_000):
#     r = random.randint(0, 51)
#     cards[r] += 1
#     card = int2card(r)
#     s = card2int(card)
#     if r != s:
#         print("Wrong!!")
#         break
# print(cards, len(cards))
