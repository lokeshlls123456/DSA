score1, score2, score3 = map(int, input().split())
scores = [score1, score2, score3]
scores.sort(reverse=True)
print(scores[1])