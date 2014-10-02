__author__ = 'markbradford'

import os
from pprint import pprint


class Parser():
    def __init__(self, start_dir, ext):
        self.start_dir = start_dir
        self.ext = ext
        self.results = []
        pass

    def set_ext(self, ext):
        """
        Setter for file extension
        """
        self.ext = str(ext)

    def parse(self):
        import os
        ext = self.ext.lower()
        for root, dirs, files in os.walk(self.start_dir):
            for f in files:
                if f.endswith(ext):
                    self.results.append(os.path.join(root, f))
        pprint(self.results)

def extra(fluff):
    return fluff.replace('\x00', '').strip()

class Mp3Info():
    def __init__(self, mp3_file, title = None, artist = None, album =None, year = None, comment = None, genre = None):
        self.mp3_file = mp3_file
        self.title = title
        self.artist = artist
        self.album = album
        self.year = year
        self.comment = comment
        self. genre = genre


    def strip_id3(self):
        """
        Read given mp3 file starting 128 characters from end and assign tag based on read position
        """
        import re
        try:
            m = open(self.mp3_file, "rb", 0)
            try:
                m.seek(-128, 2)
                m_data = m.read(128)
                self.title = extra(m_data[3:33])
                self.artist = extra(m_data[33:63])
                self.album = extra(m_data[63:93])
                self.year = extra(m_data[93:97])
                self.comment = extra(m_data[97:126])
                self.genre = re.sub(r'\D', '', (m_data[126:]))
            finally:
                m.close()
        except IOError:
            pass



if __name__ == "__main__":
   pass
