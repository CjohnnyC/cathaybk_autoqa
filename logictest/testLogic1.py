raw_score={"德瑞克":33, "尚恩":73, "傑夫":63, "馬基":39}
adjusted_score=raw_score #default

def adjust_score(score):
    new_score=None
    r=score%5
    if r>2: # r>0 and 5-r<3
       new_score=score+5-r
    elif r<=2:
        new_score=score
    
    if new_score < 40:
        return score
    else:
        return new_score

for k,v in adjusted_score.items():
    adjusted_score[k]=adjust_score(v)

print(adjusted_score)