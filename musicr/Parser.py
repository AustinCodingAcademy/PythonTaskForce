class Parser:
    def __init__(self, starting_directory, file_extension):
        self.starting_directory = starting_directory
        self.file_extension = file_extension
        self.results = []

    def start(self):