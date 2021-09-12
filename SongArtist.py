#We've given you a class called "Song" that represents
#some basic information about a song. We also wrote a 
#class called "Artist" which contains some basic 
#information about an artist.
#
#Your job is to create three instances of the song class,
#called song_1, song_2, and song_3.
#
#song_1 should have the following attributes:
#   name = "You Belong With Me"
#   album = "Fearless"
#   year = 2008
#   artist.name = "Taylor Swift"
#   artist.label = "Big Machine Records, LLC"
#
#song_2 should have the following attributes:
#   name = "All Too Well"
#   album = "Red"
#   year = 2012
#   artist.name = "Taylor Swift"
#   artist.label = "Big Machine Records, LLC"
#
#song_3 should have the following attributes:
#   name = "Up We Go"
#   album = "Midnight Machines"
#   year = 2016
#   artist.name = "LiGHTS"
#   artist.label = "Warner Bros. Records Inc."
#
#Notice, though, that song_1 and song_2 have the same
#artist and label. That means they should each have the
#SAME instance of artist: do not create separate instances
#of artist for each song.
#
#When your code is done running, there should exist three
#variables: song_1, song_2, and song_3, according to the
#requirements above.

class Artist:
    def __init__(self, name, label):
        self.name = name
        self.label = label

class Song:
    def __init__(self, name, album, year, artist):
        self.name = name
        self.album = album
        self.year = year
        self.artist = artist
        

#Write your code here!

swift = Artist("Taylor Swift", "Big Machine Records, LLC")
song_1 = Song("You Belong With Me", "Fearless", 2008, swift)
song_2 = Song("All Too Well", "Red", 2012, swift)
song_3 = Song("Up We Go", "Midnight Machines", 2016, Artist("LiGHTS", "Warner Bros. Records Inc."))


#Feel free to add code to test your code below.

for song in [song_1, song_2, song_3]:
    print(song.name, song.album, song.year, song.artist.name, song.artist.label)
    
    
    
    #####OR
    
#The key trick here is that we want to use the same instance of
#artist in both song_1 and song_2. The easiest way to do that is
#going to be to create our artists separately from our songs, then
#pass them in as arguments. So, first we create our artists...
        
artist_1 = Artist("Taylor Swift", "Big Machine Records, LLC")
artist_2 = Artist("LiGHTS", "Warner Bros. Records Inc.")

#Then we create our songs using the right instances of artist as
#the fourth argument:

song_1 = Song("You Belong With Me", "Fearless", 2008, artist_1)
song_2 = Song("All Too Well", "Red", 2012, artist_1)
song_3 = Song("Up We Go", "Midnight Machines", 2016, artist_2)

#There are other ways we could have done this. For example, we could
#have created the artist inside the Song constructor on line 25, but
#then used song_1's artist as the argument for song_2, like this:
#
#song_2 = Song("All Too Well", "Red", 2012, song_1.artist)
