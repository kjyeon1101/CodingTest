def solution(k, score):
    answer = []
    stage = []
    for s in score:
        stage.append(s)
        stage = sorted(stage, reverse=True)
        if len(stage) > k:
            stage.pop()
        answer.append(stage[min(len(stage),k)-1])
    return answer