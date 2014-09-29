<<<<<<< HEAD
__author__ = 'markbradford'
import os
from pprint import pprint

class Parser():
    def __init__(self, start_dir, file_ext):
        self.start_dir = start_dir
        self.file_ext = file_ext
        pass



    def parse(self):
        import os
        results = []
        for root, dirs, files in os.walk(self.start_dir):
            for file in files:
                if file.endswith(self.file_ext):
                    results.append(os.path.join(root, file))
        pprint(results)

    def get_results(self, results):
        return results

if __name__ == "__main__":
    start_dir = '/'
    file_ext  = '.txt'
    parse_txt = Parser(start_dir, file_ext)
    parse_txt.parse()
=======
from __future__ import print_function
import os
import string


class Parser():
    def __init__(self, ext, start_path):
        self.ext = ext
        self.start_path = start_path
        self.results = "my results"

    def parse(self, start_path, ext):


        for root, dirs, files in os.walk(start_path):
            for file in files:
                if file.endswith(ext):
                    print(os.path.join(root, file))


    def get_files(self):
        pass

    def get_results(self):
        return self.results


if __name__ == "__main__":
    myParser = Parser('.txt', '/tmp')
    print(myParser.start_path)
    print(myParser.results)
>>>>>>> dde606e00c792eb7e3fbc7d6b51456f91314e862
