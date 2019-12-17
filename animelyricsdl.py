import animelyrics


"""
CONFIG BELOW THIS TEXT
"""
CFG_TITLE = "False"
CFG_LANG = "en"
"""
CONFIG ABOVE THIS TEXT
"""

Q1_NAME = str(input("What songname? ~$ "))
Q1_ARTIST = str(input("What Artist? ~$ "))

if Q1_ARTIST != "":
    Q1_ARTIST = ""
    Q1 = str(Q1_ARTIST + " _ " + Q1_NAME)
else:
    Q1 = str(Q1_NAME)

try:
    S_LYRICS = animelyrics.search_lyrics(Q1, lang=CFG_LANG, show_title=CFG_TITLE)
except animelyrics.NoLyricsFound:
    print("FAIL!: NOT FOUND!")
except animelyrics.MissingTranslatedLyrics:
    S_LYRICS = animelyrics.search_lyrics(Q1, lang="jp", show_title=CFG_TITLE)
print(S_LYRICS)
with open('{}.txt'.format(Q1), 'w') as S_TEXT:
    S_TEXT.write(S_LYRICS)
    S_TEXT.close()
