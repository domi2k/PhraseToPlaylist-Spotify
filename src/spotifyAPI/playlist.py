from typing import Tuple, Dict, Any
import re


async def find_music_track_from_phrase(spotify, phrase, depth, current_offset=0) -> dict[Any, Any]:
    track_list = {}

    results = spotify.search(q=phrase, type='track', limit=50, offset=current_offset)

    if results['tracks']['items']:
        for track in results['tracks']['items']:
            if track['name'].lower() == phrase.lower():
                track_list = {'title': track['name'],
                              'artist': track['artists'][0]['name'],
                              'uri': track['uri']}
                break

    if (not track_list) and (results['tracks']['total'] >= current_offset) and (current_offset != depth):
        track_list = await find_music_track_from_phrase(spotify=spotify,
                                                        phrase=phrase,
                                                        depth=depth,
                                                        current_offset=current_offset + 50)

    return track_list


async def find_music_tracks(spotify, query, limit, index,
                            multiple_phrase, depth, number) -> tuple[dict[Any, Any], int, int]:
    track_list = {}
    if limit > (len(query) - index):
        limit = len(query) - index

    for current_limit in range(limit, 0, -1):
        limit = current_limit

        phrase = ' '.join(query[index:index + current_limit])
        phrase = re.sub(r'\s+([^\w\s])', r'\1', phrase)

        if not phrase[0].isalpha():
            phrase = query[index:index + 1][0]
            limit = 1

        track = await find_music_track_from_phrase(spotify=spotify, phrase=phrase, depth=depth)
        if track:
            track_list = {number: track}
            number += 1
            if multiple_phrase is False:
                break

    return track_list, limit, number


async def tracks_search(spotify, query, depth, multiple, phrases_number) -> dict[Any, Any]:
    query = re.findall(r"\w+(?:'\w+)*|[^\w\s]", query)

    current_index = 0
    number = 0

    print(query, depth, multiple, phrases_number)

    tracks = {}
    track_uris = []
    while current_index != len(query):
        cut_phrase, a, number = await find_music_tracks(spotify=spotify,
                                                        query=query,
                                                        limit=phrases_number,
                                                        index=current_index,
                                                        multiple_phrase=multiple,
                                                        depth=depth,
                                                        number=number)
        tracks.update(cut_phrase)
        track_uris.append(next(iter(cut_phrase.values()))['uri'])
        print(cut_phrase, a, next(iter(cut_phrase.values()))['uri'])
        current_index += a

    return tracks


async def create_playlist(spotify, track_uris, playlist_name):
    user_id = spotify.me()['id']
    playlist = spotify.user_playlist_create(user=user_id,
                                            name=playlist_name,
                                            public='False',
                                            description='Playlist made using PhraseToPlaylist')

    spotify.playlist_add_items(playlist_id=playlist['id'], items=track_uris)

    link = f"https://open.spotify.com/playlist/{playlist['id']}"

    return link
