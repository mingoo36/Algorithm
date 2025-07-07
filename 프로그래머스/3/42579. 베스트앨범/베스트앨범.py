from collections import defaultdict
def solution(genres, plays):
    answer = []
    
    genre_total = defaultdict(int)
    genre_songs = defaultdict(list)
    
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        genre_total[genre] += play
        genre_songs[genre].append((play, i))
    
    sorted_genres = sorted(genre_total.items(), key=lambda x: x[1], reverse=True)
    

    for genre, _ in sorted_genres:
        sorted_songs = sorted(genre_songs[genre], key=lambda x: (-x[0], x[1]))
        
        for play, idx in sorted_songs[:2]:
            answer.append(idx)
            
            
    
    return answer