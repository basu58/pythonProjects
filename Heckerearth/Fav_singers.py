noOfSongs = int(input())

playlist = list(map(int, input().split()))

frequencyOfSinger = {}

favoriteSingers = 0

for song in playlist:

    frequencyOfSinger[song] = frequencyOfSinger[song] + 1 if song in frequencyOfSinger else 1

favorite = max(frequencyOfSinger.values())

for value in frequencyOfSinger.values():

    if value is favorite:

        favoriteSingers = favoriteSingers + 1

print(favoriteSingers)

