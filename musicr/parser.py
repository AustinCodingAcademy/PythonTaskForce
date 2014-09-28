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
