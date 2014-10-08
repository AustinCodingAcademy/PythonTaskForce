import os
import sys


class Mp3Info():
    def __init__(self, filename):
        self.filename = filename
        self.tagMap = {
            "title": (3, 33, self.clean_string),
            "artist": (33, 63, self.clean_string),
            "album": (63, 93, self.clean_string),
            "year": (93, 97, self.clean_string),
            "comment": (97, 126, self.clean_string),
            "genre": (127, 128, self.translate_genre)
        }

    @staticmethod
    def clean_string(data):
        """
        Strip nulls from a given input
        :param string data: String to strip nulls from
        :return: String
        """
        return data.replace("\00", " ").strip()

    def translate_genre(self, genre_id):
        """
        Translate a genreId from its ordinal to a string
        :param int genre_id:
        :return: string
        """
        genre_id = ord(genre_id)
        with open('genre_list', 'rb', 0) as f:
            for line in f:

                found_id, genre_name = line.split("\t")
                found_id = self.clean_string(found_id)

                if str(genre_id) == str(found_id):
                    return self.clean_string(genre_name)
            return 'Unknown Genre'


    def get_tag_data(self):
        mp3Data = {}
        # If we cannot find the file, let's throw an exception
        if not os.path.exists(self.filename):
            raise Exception("File does not exist!")

        fp = open(self.filename, 'rb', 0)
        fp.seek(-128, 2)
        tagData = fp.read(128)
        fp.close()

        if tagData[:3] == 'TAG':
            for tag, (start, end, parseFunction) in self.tagMap.items():
                mp3Data[tag] = parseFunction(tagData[start:end])
            return mp3Data
        else:
            return False


if __name__ == '__main__':
    try:
        if len(sys.argv) == 1:
            raise Exception("Please specify a filename!")

        filename = sys.argv[1]

        Mp3Parser = Mp3Info(filename)
        tagData = Mp3Parser.get_tag_data()

        print tagData

    except Exception as inst:
        print "An error occurred: %s" % inst.message