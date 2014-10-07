__author__ = 'vallivallamsetla'
import os
from pprint import pprint



class Musicfinder():
    def __init__(self, starting_directory, file_extension):
        self.starting_directory = starting_directory
        self.file_extension = file_extension
        self.songs = []

    def parse(self):
        list_of_files = os.listdir(self.starting_directory)
        for root, directories, list_of_files in os.walk(self.starting_directory):
            for file in list_of_files:
                if file.endswith(self.file_extension):
                    self.songs.append(os.path.join(root, file))


    def getResults(self):
        return self.songs


if __name__ == "__main__":
    my_songs = Musicfinder("/home/vagrant/Music/", ".mp3")

    # Parse the FS
    my_songs.parse()

    pprint(my_songs.getResults())
