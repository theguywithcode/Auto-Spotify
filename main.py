import pandas as pd
from speech_recognition import Microphone, Recognizer, UnknownValueError
import spotipy as sp
from spotipy.oauth2 import SpotifyOAuth
import code as code

setup = pd.read_csv('D:\code_spotify\secrets.txt', sep='=', index_col=0, squeeze=True, header=None)
client_id = setup['client_id']
client_secret = setup['client_secret']
device_name = setup['device_name']
redirect_uri = setup['redirect_uri']
scope = setup['scope']
username = setup['username']


auth_manager = SpotifyOAuth(
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri=redirect_uri,
    scope=scope,
    username=username)
spotify = sp.Spotify(auth_manager=auth_manager)


devices = spotify.devices()
deviceID = None
for d in devices['devices']:
    d['name'] = d['name'].replace('’', '\'')
    if d['name'] == device_name:
        deviceID = d['id']
        break


r = Recognizer()
m = None
input_mic = 'pcmic (Realtek(R) Audio)'  
for i, microphone_name in enumerate(Microphone.list_microphone_names()):
    print(microphone_name,i)
    if microphone_name == input_mic:
        m = Microphone(device_index=None)
        

while True:
    """
    Commands will be entered in the specific format explained here:
     - the first word will be one of: 'album', 'artist', 'play'
     - then the name of whatever item is wanted
    """
    with m as source:
        r.adjust_for_ambient_noise(source=source)
        audio = r.listen(source=source)

    command = None
    try:
        command = r.recognize_google(audio_data=audio).lower()
    except UnknownValueError:
        continue

    print(command)
    words = command.split()
    if len(words) <= 1:
        print('Could not understand. Try again')
        continue

    name = ' '.join(words[1:])
    try:
        if words[0] == 'album':
            uri = code.get_album_uri(spotify=spotify, name=name)
            code.play_album(spotify=spotify, device_id=deviceID, uri=uri)
        elif words[0] == 'artist':
            uri = code.get_artist_uri(spotify=spotify, name=name)
            code.play_artist(spotify=spotify, device_id=deviceID, uri=uri)
        elif words[0] == 'play':
            uri = code.get_track_uri(spotify=spotify, name=name)
            code.play_track(spotify=spotify, device_id=deviceID, uri=uri)
        else:
            print('Specify either "album", "artist" or "play". Try Again')
    except code.InvalidSearchError:
        print('InvalidSearchError. Try Again')