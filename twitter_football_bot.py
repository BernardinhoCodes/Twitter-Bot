# Twitter Football Transfer rumors Bot by Bernardinho.Codes
# 1. Version without AI - offline
# have to upload the tweet manually on twiiter page - Copy/Paste

import random

part1 = ['Mane', 'Neymar', 'Lewandowski', 'Gabriel Jesus']
part2 = ['to']
part3 = ['Real Madrid?!', 'Barca!!', 'ManUtd?!', 'Juve!!', 'Chelsea?!','PSG!!', 'Bayern?!', 'Arsenal!!' 'Liverpool?!', 'ManCity!!', 'Inter?!', 'AC Milan!!']
part4 = ['Thats crazy', 'NO way', 'Not sure abt that', 'SkyItalia confirmed', 'The Sun said', 'I dnt knw abt that one', 'Woooaahh', 'Schoked right now']

tweet_constructor = [part1, part2, part3, part4]

tweet = []
for part in tweet_constructor:
    r = random.randint(0, len(part)-1)
    tweet.append(part[r])
    
print(" ".join(tweet))