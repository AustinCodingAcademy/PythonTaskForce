import os


class Parser():
    def __init__(self, root_dir, extension='mp3'):
        self.root_dir = root_dir
        self.extension = extension
        self.file_list = []
        self.stats = {'filtered_files': 0, 'total_files': 0, 'directories': 0, 'filtered_size': 0, 'total_size': 0}

    def set_extension(self, extension):
        """
        Setter for an extension filter so as to only consider files with a particular extension
        :param string extension: File extension
        :return: void
        """
        self.extension = str(extension)

    def populate_file_list(self):
        """
        Recursively populate a list of files with their full path.
        :return: bool
        """
        for root, dirs, files in os.walk(self.root_dir, topdown=False):
            for name in files:
                filename = os.path.join(root, name)
                extension = os.path.splitext(filename)[1].replace('.', '')

                self.stats['total_files'] += 1
                self.stats['total_size'] += os.path.getsize(filename) / (1024 * 1024.0)

                # Only get files that match the specified extension
                if str(extension) == str(self.extension):
                    self.file_list.append(filename)
                    self.stats['filtered_files'] += 1
                    self.stats['filtered_size'] += os.path.getsize(filename) / (1024 * 1024.0)

            # Count number of directories
            for dir_item in dirs:
                self.stats['directories'] += 1

        # Collect stats about parsed files
        self.stats['total_size'] = "%d Mb" % round(self.stats['total_size'], 2)
        self.stats['filtered_size'] = "%d Mb" % round(self.stats['filtered_size'], 2)

    def get_file_list(self):
        """
        Just get the list that was populated earlier
        :return: list
        """
        return self.file_list

    def get_stats(self):
        return self.stats
