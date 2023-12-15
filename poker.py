import random

levels = ['2','3','4','5','6','7','8','9','A','B','D','K','T']
types = ['♠','♥','♣','♦']

cards = []
for type in types:
    for level in levels:
        cards.append(level + type)

results = {}

def get_rank(card):
    if card[0] == 'A':
        rank = '10'
    elif card[0] == 'B':
        rank = '11'
    elif card[0] == 'D':
        rank = '12'
    elif card[0] == 'K':
        rank = '13'
    elif card[0] == 'T':
        rank = '14'
    else:
        rank = '0' + card[0]
    return rank + card[1]


def get_combo(part):
    part = sorted(part, key=get_rank, reverse=True)
    spades = sum(1 if card[1] == '♠' else 0 for card in part)
    hearts = sum(1 if card[1] == '♥' else 0 for card in part)
    diamonds = sum(1 if card[1] == '♦' else 0 for card in part)
    clubs = sum(1 if card[1] == '♣' else 0 for card in part)
    levels_count = [0 for a in levels]
    for card in part:
        levels_count[levels.index(card[0])] += 1
    straight_pos = [idx + 1 for idx, _ in enumerate(levels_count) if levels_count[idx:idx + 5] == [1, 1, 1, 1, 1]]
    is_straight = len(straight_pos) > 0
    is_royal_flush = is_straight and min(straight_pos) == 9 and sum([1 if part[i][1] == part[0][1] else 0 for i in range(5)]) == 5
    is_kare = 4 in levels_count
    is_full_house = 2 in levels_count and 3 in levels_count
    is_flush = max(spades, hearts, diamonds, clubs) >=5
    is_set = 3 in levels_count
    is_two_pairs = levels_count.count(2) >= 2
    is_pair = levels_count.count(2) == 1
    if is_royal_flush:
        return 'royal flush'
    elif is_straight and is_flush:
        return 'straight flush'
    elif is_kare:
        return 'kare'
    elif is_full_house:
        return 'full house'
    elif is_flush:
        return 'flush'
    elif is_straight:
        return 'straight'
    elif is_set:
        return 'set'
    elif is_two_pairs:
        return 'two pairs'
    elif is_pair:
        return 'pair'
    else:
        return 'high hand'

mmm = 100000000
for i in range(mmm):
    combo = get_combo(random.sample(cards, 7))
    if combo not in results:
        results[combo] = 1
    else:
        results[combo] += 1
for k, v in sorted(results.items(), key=lambda item: item[1], reverse=True):
    print(k, v / mmm * 100)