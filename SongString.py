#Below are the two class definitions we supplied previously:
#Artist and Song.
#
#Write a function called "get_song_string". It should accept
#one argument which will be a Song object. It should return
#a string in the following format:
#
# "<song name>" - <artist name> (<song year>)
# e.g: 
# "You Belong With Me" - Taylor Swift (2008)
#
#The quotation marks around the song title should be *part*
#of the string.
#
#Hint: You're writing a function, not a method. That means
#the function get_song_string should not be inside either
#of these classes.

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

def get_song_string(song):
    return '"{}" - {} ({})'.format(song.name, song.artist.name, song.year)
        
#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: "You Belong With Me" -Taylor Swift (2008)
new_artist = Artist("Taylor Swift", "Big Machine Records, LLC")
new_song = Song("You Belong With Me", "Fearless", 2008, new_artist)
print(get_song_string(new_song))


###OR


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

#This function can actually be written in only a single line.
#First, we declare the function:
def get_song_string(a_song):
    
    #Then, we create the string. Since we want to use quotation
    #marks inside the string, we'll use apostrophes to create
    #our string. 
    #return '"' + a_song.name + '" - ' + a_song.artist.name + ' (' + str(a_song.year) + ')'

    #We could also use our alternative string formatting syntax,
    #which makes this even easier to read:
    #
    return '"{0}" - {1} ({2})'.format(a_song.name, a_song.artist.name, a_song.year)
        
#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: "You Belong With Me" -Taylor Swift (2008)
new_artist = Artist("Taylor Swift", "Big Machine Records, LLC")
new_song = Song("You Belong With Me", "Fearless", 2008, new_artist)
print(get_song_string(new_song))
