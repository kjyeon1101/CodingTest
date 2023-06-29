def solution(cards1, cards2, goal):
    card = []
    for g in goal:
        if g in cards1 and cards1.index(g) == 0:
            card.append(cards1.pop(0))
        if g in cards2 and cards2.index(g) == 0:
            card.append(cards2.pop(0))
    answer = "Yes" if card == goal else "No"
    return answer