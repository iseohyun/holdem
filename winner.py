import os
import ast
import datetime
from rank import get_rank
from cvt import card2int, int2card

my_hand_set = [
    # ["As", "Ac"],
    # ["Ks", "Kc"],
    # ["Qs", "Qc"],
    # ["Js", "Jc"],
    ["Ts", "Tc"],
    ["9s", "9c"],
    ["8s", "8c"],
    ["7s", "7c"],
    ["6s", "6c"],
    ["5s", "5c"],
    ["4s", "4c"],
    ["3s", "3c"],
    ["2s", "2c"],
    ["As", "Ks"],
    ["As", "Qs"],
    ["As", "Js"],
    ["As", "Ts"],
    ["As", "9s"],
    ["As", "8s"],
    ["As", "7s"],
    ["As", "6s"],
    ["As", "5s"],
    ["As", "4s"],
    ["As", "3s"],
    ["As", "2s"],
    ["Ks", "Qs"],
    ["Ks", "Js"],
    ["Ks", "Ts"],
    ["Ks", "9s"],
    ["Ks", "8s"],
    ["Ks", "7s"],
    ["Ks", "6s"],
    ["Ks", "5s"],
    ["Ks", "4s"],
    ["Ks", "3s"],
    ["Ks", "2s"],
    ["Qs", "Js"],
    ["Qs", "Ts"],
    ["Qs", "9s"],
    ["Qs", "8s"],
    ["Qs", "7s"],
    ["Qs", "6s"],
    ["Qs", "5s"],
    ["Qs", "4s"],
    ["Qs", "3s"],
    ["Qs", "2s"],
    ["Js", "Ts"],
    ["Js", "9s"],
    ["Js", "8s"],
    ["Js", "7s"],
    ["Js", "6s"],
    ["Js", "5s"],
    ["Js", "4s"],
    ["Js", "3s"],
    ["Js", "2s"],
    ["Ts", "9s"],
    ["Ts", "8s"],
    ["Ts", "7s"],
    ["Ts", "6s"],
    ["Ts", "5s"],
    ["Ts", "4s"],
    ["Ts", "3s"],
    ["Ts", "2s"],
    ["9s", "8s"],
    ["9s", "7s"],
    ["9s", "6s"],
    ["9s", "5s"],
    ["9s", "4s"],
    ["9s", "3s"],
    ["9s", "2s"],
    ["8s", "7s"],
    ["8s", "6s"],
    ["8s", "5s"],
    ["8s", "4s"],
    ["8s", "3s"],
    ["8s", "2s"],
    ["7s", "6s"],
    ["7s", "5s"],
    ["7s", "4s"],
    ["7s", "3s"],
    ["7s", "2s"],
    ["6s", "5s"],
    ["6s", "4s"],
    ["6s", "3s"],
    ["6s", "2s"],
    ["5s", "4s"],
    ["5s", "3s"],
    ["5s", "2s"],
    ["4s", "3s"],
    ["4s", "2s"],
    ["3s", "2s"],
    ["As", "Kc"],
    ["As", "Qc"],
    ["As", "Jc"],
    ["As", "Tc"],
    ["As", "9c"],
    ["As", "8c"],
    ["As", "7c"],
    ["As", "6c"],
    ["As", "5c"],
    ["As", "4c"],
    ["As", "3c"],
    ["As", "2c"],
    ["Ks", "Qc"],
    ["Ks", "Jc"],
    ["Ks", "Tc"],
    ["Ks", "9c"],
    ["Ks", "8c"],
    ["Ks", "7c"],
    ["Ks", "6c"],
    ["Ks", "5c"],
    ["Ks", "4c"],
    ["Ks", "3c"],
    ["Ks", "2c"],
    ["Qs", "Jc"],
    ["Qs", "Tc"],
    ["Qs", "9c"],
    ["Qs", "8c"],
    ["Qs", "7c"],
    ["Qs", "6c"],
    ["Qs", "5c"],
    ["Qs", "4c"],
    ["Qs", "3c"],
    ["Qs", "2c"],
    ["Js", "Tc"],
    ["Js", "9c"],
    ["Js", "8c"],
    ["Js", "7c"],
    ["Js", "6c"],
    ["Js", "5c"],
    ["Js", "4c"],
    ["Js", "3c"],
    ["Js", "2c"],
    ["Ts", "9c"],
    ["Ts", "8c"],
    ["Ts", "7c"],
    ["Ts", "6c"],
    ["Ts", "5c"],
    ["Ts", "4c"],
    ["Ts", "3c"],
    ["Ts", "2c"],
    ["9s", "8c"],
    ["9s", "7c"],
    ["9s", "6c"],
    ["9s", "5c"],
    ["9s", "4c"],
    ["9s", "3c"],
    ["9s", "2c"],
    ["8s", "7c"],
    ["8s", "6c"],
    ["8s", "5c"],
    ["8s", "4c"],
    ["8s", "3c"],
    ["8s", "2c"],
    ["7s", "6c"],
    ["7s", "5c"],
    ["7s", "4c"],
    ["7s", "3c"],
    ["7s", "2c"],
    ["6s", "5c"],
    ["6s", "4c"],
    ["6s", "3c"],
    ["6s", "2c"],
    ["5s", "4c"],
    ["5s", "3c"],
    ["5s", "2c"],
    ["4s", "3c"],
    ["4s", "2c"],
    ["3s", "2c"],
]

values = "AKQJT98765432"
test_code = [0, 0]


def get_winner(players, board):
    """
    >>> get_winner([['As', 'Ac'],['3s', '2c']], ['Ks', '8c', '3d', 'Jh', '6c'])
    [0]
    >>> get_winner([['Ks', '5c'],['Ks', '2c']], ['Kd', '8c', '3d', 'Jh', '6c'])
    [0, 1]
    >>> get_winner([['Ks', '5c'],['Ks', 'Kc']], ['Kd', '8c', '3d', 'Jh', '6c'])
    [1]
    >>> get_winner([["Ah", "Ad"], ["Qs", "8d"]], ["Ac", "Jh", "2s", "9d", "Tc"])
    [1]
    """
    ranks = []
    for player in players:
        ranks.append(get_rank(player + board))

    best_rank = ranks[0]  # 0번 임시 우승
    winner = [0]  # split(동시 우승) 가능성 있음

    for i in range(1, len(ranks)):  # 1부터 챌린지
        current_rank = ranks[i]
        if current_rank[0] < best_rank[0]:  # 랭킹 우위
            best_rank = current_rank  # 우승자 변경
            winner = [i]  # 우승자 목록 단독 기록
            # if(best_rank[0] == 1): # Test Code
            # test_code[0] += 1 # Test Code
        elif current_rank[0] == best_rank[0]:  # 동일 랭킹, 하이카드 비교
            for cur, best in zip(current_rank[1], best_rank[1]):
                if values.index(cur) < values.index(best):  # 새 우승자 탄생
                    best_rank = current_rank
                    winner = [i]
                    break
                elif values.index(cur) > values.index(best):
                    break
            else:
                winner.append(i)  # 공동 우승자 탄생

    return winner


def cnt_winner(players, board=["", "", "", "", ""]):
    """players, 카드 숫자로 넘어온다.(예)[[0,1],[2,3]]"""
    outs = [i for i in range(52)]
    winner_count = [0 for _ in range(len(players))]

    # players의 hand를 문자열로 바꾼다.
    for player in players:
        for i in range(2):
            outs.remove(player[i])
            player[i] = int2card(player[i])

    tot_match = 0
    for flop1 in range(0, len(outs) - 4):
        board[0] = int2card(outs[flop1])
        for flop2 in range(flop1 + 1, len(outs) - 3):
            board[1] = int2card(outs[flop2])
            for flop3 in range(flop2 + 1, len(outs) - 2):
                board[2] = int2card(outs[flop3])
                for turn in range(flop3 + 1, len(outs) - 1):
                    board[3] = int2card(outs[turn])
                    for river in range(turn + 1, len(outs)):
                        board[4] = int2card(outs[river])
                        winners = get_winner(players, board)
                        for winner in winners:
                            winner_count[winner] += 1

    # players의 hand를 숫자로 바꾼다.
    for player in players:
        for i in range(2):
            player[i] = card2int(player[i])

    # print(test_code) # test Code: 테스트 결과 출력력
    return winner_count


def print_file(my_hand):
    dir = "98_Examples/holdem/out"
    filename = f"{dir}/{my_hand[0]}{my_hand[1]}.txt"
    players = [[card2int(my_hand[0]), card2int(my_hand[1])], [0, 0]]

    # 초기 파일 생성 (없을 경우)
    if not os.path.exists(filename):
        with open(filename, "w") as f:
            f.write("")

    with open(filename, "r") as f:
        lines = f.readlines()

    # 마지막 기록된 hand 가져오기
    if lines:
        last_record = lines[-1]
        print("last record: ", last_record)
        last_record = ast.literal_eval(f"[{last_record}]")
        players[1] = [card2int(last_record[0][0]), card2int(last_record[0][1])]
        print(players)
    else:
        players[1] = [0, 0]

    start_processing = False

    outs = [x for x in range(52)]
    outs.remove(players[0][0])
    outs.remove(players[0][1])
    last_time = datetime.datetime.now()

    for i in range(50):
        if (not start_processing) and outs[i] < players[1][0]:
            continue

        patterns = []
        for j in range(i + 1, 50):
            if not start_processing:
                if outs[j] <= players[1][1]:
                    if j == 49:
                        start_processing = True
                        print(">> Start process: ", players)
                    continue
                    
                start_processing = True
                print(">> Start process: ", players)

            players[1] = [outs[i], outs[j]]
            cur_pattern = get_pattern(players)
            message_out = f"\n['{int2card(players[1][0])}', '{int2card(players[1][1])}'], "

            for k, pattern in enumerate(patterns):
                if cur_pattern == pattern:
                    search_text = f"{int2card(outs[i])}', '{int2card(outs[j] -len(patterns) + k)}"
                    with open(filename, "r") as f:
                        for line in f:
                            if search_text in line:
                                winner_count = ast.literal_eval(f"[{line}]")[1]
                                message_out += f"{winner_count}, '*'"
                                break
                    break
            else:
                winner_count = cnt_winner(players)
                message_out += f"{winner_count}"

            with open(filename, "a") as f:
                f.write(message_out)

            if outs[j] % 4 == 3:
                patterns = []
            else:
                patterns.append(cur_pattern)
            
            current_time = datetime.datetime.now()
            time_diff =  current_time - last_time
            print(f"[{current_time}({time_diff.seconds})]: {message_out[1:]}")
            last_time = current_time


def get_pattern(players):
    """pattern = ### : 1 처음 등장한 카드(s), 2 두번째 등장한 카드()
    첫 카드는 항상 처음 등장(spades)
    2번째 카드는 항상 (spades 또는 clubs)
    예시: [(1)111, (1)112, 121, 122, 123, 211, 212, 222, 223, 233, 234]
    
    >>> get_pattern([[0, 1], [2, 3]])
    234
    >>> get_pattern([[12, 16], [42, 43]])
    123
    >>> get_pattern([[12, 16], [42, 41]])
    123
    >>> get_pattern([[19, 21], [23, 25]])
    232
    """
    order = [1, 0, 0, 0]

    if(players[0][1] % 4 == 0):
        pattern = 10
    else:
        order[1] = 2
        pattern = 20

    if order[players[1][0] % 4] == 0:
        order[players[1][0] % 4] = max(order) + 1

    pattern += order[players[1][0] % 4]
    pattern *= 10

    if order[players[1][1] % 4] == 0:
        order[players[1][1] % 4] = max(order) + 1

    pattern += order[players[1][1] % 4]

    return pattern


def create_data_thread():
    threads = []

    for my_hand in my_hand_set:
        thread = threading.Thread(target=print_file, args=([my_hand]))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


# create_data_thread()

def create_data():
    for my_hand in my_hand_set:
        print_file(my_hand)

create_data()

import doctest

# print(doctest.testmod())
