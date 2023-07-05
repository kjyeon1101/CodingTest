def solution(genres, plays):
    genres_plays = dict()
    i = 0
    
    for g, p in zip(genres, plays):
        if genres_plays.get(g) == None:
            genres_plays[g] = [(i, p)]
        else:
            genres_plays[g] += [(i, p)]
        i += 1
    
    for gps in genres_plays:
        genres_plays[gps] = sorted(genres_plays[gps], key=lambda x:(-x[1], x[0]))
    genres_plays = sorted(genres_plays.items(), key = lambda x: -sum([i[1] for i in x[1]]))
    
    answer = [g[0] for gps in genres_plays for g in gps[1][:2]]
            
    return answer