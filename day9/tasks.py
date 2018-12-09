from llist import dllist

import time

def game_rules(round: dllist, current_marble, next_marble):
    score = 0
    if next_marble % 23 == 0:
        score += next_marble
        node = current_marble
        for i in range(7):
            node = node.prev
            if node == None:
                node = round.last
        score += node.value
        current_marble = node.next
        round.remove(node)
    else:
        next_step = current_marble.next
        if next_step is None:
            if len(round)>1:
                next_step = round.nodeat(1)
            else:
                next_marble = None
        else:
            next_step = next_step.next
        current_node =  next_step
        current_marble = round.insert(next_marble, current_node)
    return (round, current_marble, score)


def create_players(number):
    return [
        { 
            "player": i + 1,
            "score" : 0
        } for i in range(number)
    ]


def play_game(num_players, last_marble, show_time=False):
    players = create_players(num_players)
    round = dllist([0, 1])
    next_marble = 2
    current_marble = round.nodeat(1)
    player_index = 0
    count =0
    start = time.time()
    while last_marble >= next_marble:
        count +=1
        if count % 100000== 0 and show_time:
            print(count)
            end = time.time()
            print(end - start)
            start = time.time()
        (round, current_marble, score) = game_rules(round, current_marble, next_marble)
        players[player_index]['score'] += score
        player_index = (player_index + 1) % num_players
        next_marble +=1
    return players

def highscore(players):
    max = 0
    for player in players:
        if player['score'] > max:
            max = player['score']
    return max

assert highscore(play_game(10, 1618)) == 8317
assert highscore(play_game(13, 7999)) == 146373
assert highscore(play_game(17, 1104)) == 2764
assert highscore(play_game(21, 6111)) == 54718
assert highscore(play_game(30, 5807)) == 37305


f = open('task.data', 'r')
data = []
for line in f:
    numbers = line.replace('\n','').split(' ')
    data.append(int(numbers[0]))
    data.append(int(numbers[6]))
f.close()


print(f"Task 1: {highscore(play_game(data[0], data[1]))}")
print(f"Task 2: {highscore(play_game(data[0], data[1]*100))}")
