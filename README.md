<br/>

<h3 align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://github.com/domi2k/PhraseToPlaylist-Spotify/blob/main/assets/logo_light.png" height="100">
    <source media="(prefers-color-scheme: light)" srcset="https://github.com/domi2k/PhraseToPlaylist-Spotify/blob/main/assets/logo_dark.png" height="100">
    <img alt="PhraseToPlaylist" src="https://github.com/domi2k/PhraseToPlaylist-Spotify/blob/main/assets/logo_light.png" height="100">
  </picture>
</h3>

<br/>

<p align="center">
	PhraseToPlaylist transforms the entered text into Spotify playlist in which the song titles represent the exact phrase you entered.
</p>

<p align="center">
  <a href="https://github.com/domi2k/PhraseToPlaylist-Spotify/stargazers"><img src="https://img.shields.io/github/stars/domi2k/PhraseToPlaylist-Spotify?colorA=363a4f&colorB=ffffff&style=for-the-badge"></a>&nbsp;
  <a href="https://github.com/domi2k/PhraseToPlaylist-Spotify/issues"><img src="https://img.shields.io/github/issues/domi2k/PhraseToPlaylist-Spotify?colorA=363a4f&colorB=ffffff&style=for-the-badge"></a>&nbsp;
  <a href="https://discordapp.com/users/329876941631127554"><picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://img.shields.io/badge/-Discord-FFFFFF?style=for-the-badge&logo=Discord&logoColor=black">
    <source media="(prefers-color-scheme: light)" srcset="https://img.shields.io/badge/-Discord-000000?style=for-the-badge&logo=Discord&logoColor=white">
    <img src="https://img.shields.io/badge/-Discord-FFFFFF?style=for-the-badge&logo=Discord&logoColor=black"/>
  </picture></a>&nbsp;
</p>

<br/>

![Website Preview](https://github.com/domi2k/PhraseToPlaylist-Spotify/blob/main/assets/preview.png)

##

To use **PhraseToPlaylist**, start your Flask server and navigate to the homepage. Enter the phrase you want to transform into a playlist. Choose options for your search, wait for the system to find suitable tracks, and click the button to create your playlist.

## Installation

To set up your development environment, follow these steps:
- Clone this repository
```bash
git clone https://github.com/domi2k/PhraseToPlaylist-Spotify
```
- Create a new account or log in on https://developers.spotify.com/.
- Go to the [dashboard](https://developer.spotify.com/dashboard) and create an application.
- Add a redirect URI to your application at [dashboard](https://developer.spotify.com/dashboard).
```
http://127.0.0.1:8080
```
- Copy your new ID and SECRET and add them to your environment.
``` bash
export SPOTIPY_CLIENT_ID=your_client_id
export SPOTIPY_CLIENT_SECRET=your_client_secret
export SPOTIPY_REDIRECT_URI='http://127.0.0.1:8080'
```
> **Note**
> On Windows, use `SET` instead of `export`

If you have a problem with the port or would like to set a different one, you will need to update your Spotify Application at [dashboard](https://developer.spotify.com/dashboard), the **SPOTIPY_REDIRECT_URI** variable and change the port value in the `run.py` file:
```py
from src import create_app

app = create_app()

if __name__ == '__main__':
    app.run(port=8080)
```
Located in the main folder:
```
├── src/
├── instance/
├── run.py <---
└── ...
```

## Requirements

This project requires `Python 3.12` and the latest versions of `Flask` and `Spotipy`. All necessary libraries are listed in the `requirements.txt` file.

To install all required Python libraries, you can use pip:

```bash
pip install -r requirements.txt
```

## Contact

If you have any questions about this project, feel free to contact me on 'Discord'.

<p align="center">
  <a href="https://discordapp.com/users/329876941631127554"><picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://img.shields.io/badge/-Discord-FFFFFF?style=for-the-badge&logo=Discord&logoColor=black">
    <source media="(prefers-color-scheme: light)" srcset="https://img.shields.io/badge/-Discord-000000?style=for-the-badge&logo=Discord&logoColor=white">
    <img src="https://img.shields.io/badge/-Discord-FFFFFF?style=for-the-badge&logo=Discord&logoColor=black"/>
  </picture></a>&nbsp;
</p>

## ⚠︎ Disclaimer ⚠︎

This project is not affiliated, associated, authorized, endorsed by, or in any way officially connected with **Spotify**. PhraseToPlaylist is an independent project.


&nbsp;

<p align="center">
  <a href="https://github.com/domi2k/PhraseToPlaylist-Spotify/blob/main/LICENSE">
    <img src="https://img.shields.io/static/v1.svg?style=for-the-badge&label=License&message=GPL-3.0&colorA=363a4f&colorB=ffffff"/>
  </a>
</p>
<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://github.com/domi2k/PhraseToPlaylist-Spotify/blob/main/assets/footer_light.png">
    <source media="(prefers-color-scheme: light)" srcset="https://github.com/domi2k/PhraseToPlaylist-Spotify/blob/main/assets/footer_dark.png">
    <img alt="Footer" src="https://github.com/domi2k/PhraseToPlaylist-Spotify/blob/main/assets/footer_light.png">
  </picture>
</p>