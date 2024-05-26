from flask import Blueprint, render_template, request, redirect, session
from ..services.spotify_service import search_for_tracks, create_playlist
import spotipy

bp = Blueprint('routes', __name__)


def authorization():
    scope = 'playlist-modify-private playlist-modify-public'
    cache_handler = spotipy.cache_handler.FlaskSessionCacheHandler(session)
    auth_manager = spotipy.oauth2.SpotifyOAuth(cache_handler=cache_handler, scope=scope, show_dialog=True)

    return auth_manager, cache_handler


@bp.route('/', methods=['GET', 'POST'])
def home():
    auth_manager, cache_handler = authorization()

    if request.args.get("code"):
        auth_manager.get_access_token(request.args.get("code"))
        return redirect('/')

    if not auth_manager.validate_token(cache_handler.get_cached_token()):
        auth_url = auth_manager.get_authorize_url()
        return render_template('base.html', auth_url=auth_url)

    spotify = spotipy.Spotify(auth_manager=auth_manager)

    return render_template('base.html', profile=spotify.me())


@bp.route('/sign_out')
def sign_out():
    session.pop("token_info", None)
    return redirect('/')


@bp.route('/searching_tracks', methods=['POST'])
def searching():
    auth_manager, cache_handler = authorization()

    if not auth_manager.validate_token(cache_handler.get_cached_token()):
        return redirect('/')

    spotify = spotipy.Spotify(auth_manager=auth_manager)

    data = request.json
    print(data)

    return search_for_tracks(spotify=spotify, data=data)


@bp.route('/create_playlist', methods=['POST'])
def playlist():
    auth_manager, cache_handler = authorization()

    if not auth_manager.validate_token(cache_handler.get_cached_token()):
        return redirect('/')

    spotify = spotipy.Spotify(auth_manager=auth_manager)

    data = request.json
    print(data)

    return create_playlist(spotify=spotify, data=data)
