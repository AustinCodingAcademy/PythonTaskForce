import os



class FileParser():
    def __init__(self, root_dir, extension):
        self.root_dir = root_dir
        self.extension = extension
        self.file_list = []
        self.stats = {'filtered_files': 0, 'total_files': 0, 'directories': 0, 'filtered_size': 0, 'total_size': 0}

    def set_extension_filter(self, extension):
        """
        set an extension filter so as to only consider files with a particular extension
        :param string extension: File extension
        :return: void
        """
        self.extension = str(extension)

    def populate_file_list(self):
        """
        Populate a list of files with their full path.
        Recurse into sub-folders
        :return: bool
        """
        for root, dirs, files in os.walk(self.root_dir, topdown=False):
