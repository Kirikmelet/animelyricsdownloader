#!/usr/bin/env python
import argparse
import animelyrics


# argparse stuff

PARSER = argparse.ArgumentParser(
        description="Downloads animelyrics to a text file\n! '-a' does not work !")
PARSER.add_argument(
        '-s', '--song',
        action='store',
        dest="song",
        type=str,
        required=True)
PARSER.add_argument(
        '-a', '--artist',
        action='store',
        type=str,
        dest="artist",
        required=False)
PARSER.add_argument(
        '-l', '--language',
        choices=[
            'english',
            'en',
            'japanese',
            'jp'],
        action='store',
        dest='language',
        help='prints with language \n defaults to English')
PARSER.add_argument(
        '-T', '--title',
        action='store_true',
        dest='title',
        help='Prints Title')
ARG = PARSER.parse_args()

def lyrics_d(group_master):
    '''Lyric Downloader '''
    lyrics = animelyrics.search_lyrics(group_master, lang=LANG, show_title=TITLE)
    with open((group_master +'.txt'), 'w') as txt_lyrics:
        txt_lyrics.write(lyrics)
        txt_lyrics.close()

if __name__ == "__main__":
    if (ARG.language == 'jp') or (ARG.language == 'japanese'):
        LANG = 'jp'
    else:
        LANG = 'en'
    if ARG.title != True:
        TITLE = False
    else:
        TITLE = True
    ARTIST_T = ARG.artist
    SONG_T = ARG.song
    T = str(SONG_T)
    print(T)
    lyrics_d(T)
