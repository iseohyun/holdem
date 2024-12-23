values = "AKQJT98765432"
shapes = "schd"


def get_rank(cards):
    """
    >>> get_rank(["Kh", "Ah", "6h", "Qh", "Th", "Jh", "2h"])
    [0, 'AKQJT']
    >>> get_rank(["3h", "Ah", "6h", "5h", "4h", "3h", "2h"])
    [1, '65432']
    >>> get_rank(["3h", "Ah", "6s", "5h", "4h", "3h", "2h"])
    [1, '5432A']
    >>> get_rank(["3h", "Kh", "Ks", "Kd", "Kc", "Qh", "2h"])
    [2, 'KKKK']
    >>> get_rank(["3h", "Qd", "Js", "Jd", "Jc", "Qh", "3h"])
    [3, 'JJJQQ']
    >>> get_rank(["3h", "Ah", "6s", "5h", "9h", "Kh", "2h"])
    [4, 'AK953']
    >>> get_rank(["3s", "Ah", "6s", "5d", "4d", "3h", "2h"])
    [5, '65432']
    >>> get_rank(["3s", "Ah", "9s", "5d", "4d", "3h", "2h"])
    [5, '5432A']
    >>> get_rank(["3h", "Qd", "Js", "Jd", "Jc", "8h", "Ah"])
    [6, 'JJJAQ']
    >>> get_rank(["3h", "Qd", "Js", "Jd", "Ac", "8h", "Ah"])
    [7, 'AAJJQ']
    >>> get_rank(["3h", "Qd", "Js", "Jd", "Ac", "8h", "9h"])
    [8, 'JJAQ9']
    >>> get_rank(["3h", "Qd", "Js", "6d", "Ac", "8h", "9h"])
    [9, 'AQJ98']
    """
    # 정렬) 기준1: value[A ~ 2], 기준2: shape(spade, club, heart, diamond)
    cards = sorted(cards, key=lambda x: (values.index(x[0]), shapes.index(x[1])))
    flush = ""
    triple = ""

    deck = is_flush(cards)
    if deck and len(deck) > 0:
        straight = is_straight(deck)
        if straight and len(straight) > 0:
            if straight == "AKQJT":
                return [0, straight]  # 0. "R. Flush"
            return [1, straight]  # 1. "S. Flush"
        # 보류: four-card와 Full house를 검사 한 후에 없으면 출력한다.
        flush = [4, deck[0:5]]  # 4. "Flush"

    deck = "".join(card[0] for card in cards)
    for i in range(len(deck) - 2):
        if deck[i] == deck[i + 1] == deck[i + 2]:  # 연속된 3개 문자가 같으면
            if i + 3 < len(deck) and deck[i] == deck[i + 3]:  # 연속된 4개 문자가 같으면
                return [2, deck[i : i + 4]]  # 2. "Four of Card"
            else:
                for j in range(len(deck) - 1):
                    if j == i or j == i + 1 or j == i + 2:
                        continue
                    elif deck[j] == deck[j + 1]:
                        return [3, deck[i] * 3 + deck[j] * 2]  # 3. "Full House"
            triple = deck[i : i + 3]
            break

    if flush != "":
        return flush  # 4

    straight = is_straight(deck)
    if straight and len(straight) > 0:
        return [5, straight]  # 5. "Straight"

    if triple != "":
        return [6, triple + deck.replace(triple, "")[0:2]]  # 6. "Triple"

    for i in range(len(deck) - 1):
        if deck[i] == deck[i + 1]:
            pair = deck[i] * 2
            deck = deck.replace(deck[i], "")
            for j in range(len(deck) - 1):
                if deck[j] == deck[j + 1]:
                    pair += deck[j] * 2
                    deck = deck.replace(deck[j], "")
                    return [7, pair + deck[0]]  # 7. "Two pair"
            return [8, pair + deck[0:3]]  # 8. "One pair"

    return [9, deck[0:5]]  # 9. "High card"


def is_straight(deck):
    # 중복되는 value를 삭제한다.
    deck = "".join(sorted(set(deck), key=deck.index))

    # straight를 찾는다.
    for i in range(len(deck) - 4):
        if deck[i : i + 5] in values:
            return deck[i : i + 5]

    # back-straight가 있는지 찾는다.
    if "5432" in deck and "A" in deck:
        return "5432A"

    return False


def is_flush(cards):
    shape = [0, 0, 0, 0]
    for card in cards:  # shape별 count
        match card[1]:
            case "s":
                shape[0] += 1
            case "c":
                shape[1] += 1
            case "h":
                shape[2] += 1
            case "d":
                shape[3] += 1

    for i, count in enumerate(shape):
        if count >= 5:
            flush_suit = shapes[i]
            # 해당 문양의 카드만 모으기
            return "".join(card[0] for card in cards if card[1] == flush_suit)

    return ""


import doctest

resault = doctest.testmod()  # automatically validate the embedded tests
print(resault)
