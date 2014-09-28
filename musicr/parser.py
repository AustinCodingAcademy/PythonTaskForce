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