import pylast  
import time
import datetime
import credentials
import sys

password_hash = pylast.md5(credentials.password)

network = pylast.LastFMNetwork( api_key = credentials.API_KEY,
                                api_secret = credentials.API_SECRET,
                                username = credentials.username,
                                password_hash = password_hash)

scrobble_file = open(sys.argv[1], 'r' )
failures = open(sys.argv[1] + "_failed", 'w' )

for scrobble in scrobble_file:
    if scrobble[0] != "#":
        scrobble_parts = scrobble.split("\t")
        artist = 
        time = int(scrobble_parts[-2])
        network.scrobble(artist= "Iron Maiden", title="The Nomad",
         timestamp=time)
    else:
        failures.write(scrobble)


scrobble_file.close()
