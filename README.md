<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/theguywithcode/Auto-Spotify.git">
    <img src="https://www.freepnglogos.com/uploads/spotify-logo-png/image-gallery-spotify-logo-21.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Auto-Spotify using Voice Recognition</h3>

  <p align="center">
    A Simple Script that will help you to Play /  Change Songs with just your Voice 
    <br />
    <a href="https://github.com/theguywithcode/Auto-Spotify.git"><strong>Explore the docs »</strong></a>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#Future-Updates">Future Updates</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project



Tired of Switching tabs  for changing a particular song or play some song that bring the kick in your task !!!

Well Same was with me Tired of Switching tabs and loosing focus from studying / Coding something Great...

<p>As a Result here is <b>Auto-Spotify !!! </b></p>

 A Simple Script that will help you to Play / Change Songs with just your Voice. 

Here's why you should using this:
* Your time should be focused on creating something amazing rather than switching tabs  & Changing songs. 
* You shouldn't be doing the same tasks over and over like searching for song & Playing it 
* You should Simply say Song name or an Artist name or a Playlist name & Song should play along :smile:

### Built With

This section should list any major frameworks that you built your project using. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.
* [Spotify API](https://https://developer.spotify.com/)
* [PyAudio](https://pypi.org/project/PyAudio/)
* [Speech Recognition](https://pypi.org/project/SpeechRecognition/)



<!-- GETTING STARTED -->
## Getting Started

Few Steps Before you can Start using this !!!

**Note** - Only Works With Premium Spotify Account.

### Prerequisites

Hoping you Have your Premium Spotify Account !!!<br>
* Go to [Spotify Developer](https://https://developer.spotify.com/)  and setup your developer Profile.<br>
  <img src="https://i.ibb.co/dB1TVgr/devspotify.png" alt="devspotify" border="0">
* Once you create an App, Go to Edit Settings,there Fill following details
  <img src="https://i.ibb.co/QvNWfqj/image.png" alt="Edit Settings" border="0"></a>

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/theguywithcode/code_spotify.git
   ```
2. Install PIP packages
   ```sh
   pip install PyAudio
   ```
    ```sh
   pip install spotipy   
   ```
    ```sh
   pip install SpeechRecognition    
   ```
   
3. Create a Python file called *secrets.py*, In this file, enter all of the values of the required variables in the following format:
    
    ```sh
    client_id=XXXXX
    client_secret=XXXXX
    device_name=Device Name
    redirect_uri= https://codeguy.me/callback/
    username= Spotify Username
    scope=user-read-private user-read-playback-state user-modify-playback-state user-library-read  
   ```


<!-- USAGE EXAMPLES -->
## Usage

Install all Python Libraries and also create  *secrets.py* file and replace the content inside the file

Run the follwoing command in your terminal
 ```sh 
    python main.py
```

* Commands will be entered in the specific format explained here:
     - the first word will be one of: 'album', 'artist', 'play'
     - then the name of whatever item is wanted



<!-- Updates -->
## Future-Updates

* GUI Application.
* More Functionality.




<!-- CONTACT -->
## Contact

Your Name - [@Theguywithcode](https://twitter.com/Theguywithcode) - help@codeguy.me

Project Link: [Auto-Spotify](https://github.com/theguywithcode/Auto-Spotify.git)
