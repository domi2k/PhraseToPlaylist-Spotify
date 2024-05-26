import asyncio
from flask import jsonify
from ..spotifyAPI import playlist


def search_for_tracks(spotify, data):
    if all(key in data for key in ['searchQuery', 'multipleSearching', 'searchDepth', 'phrasesNumber']):
        search_query = data.get('searchQuery')
        search_depth = int(data.get('searchDepth'))
        multiple_search = bool(data.get('multipleSearching'))
        phrases_number = int(data.get('phrasesNumber'))

        tracks = asyncio.run(playlist.tracks_search(spotify=spotify,
                                                    query=search_query,
                                                    depth=search_depth,
                                                    multiple=multiple_search,
                                                    phrases_number=phrases_number))

        print(tracks)

        return jsonify({'status': 'success', 'tracks': tracks}), 200
    else:
        return jsonify({'status': 'error'}), 400


def create_playlist(spotify, data):
    try:
        track_uris = [details['uri'] for details in data['tracks'].values()]

        if data['playlistName']:
            playlist_name = data['playlistName']
        else:
            playlist_name = "Generated playlist"

        link = asyncio.run(playlist.create_playlist(spotify=spotify,
                                                    track_uris=track_uris,
                                                    playlist_name=playlist_name))

        return jsonify(link), 200
    except Exception as e:
        return jsonify({'status': e}), 400
