import os

"""
This class will parse through directories on the file system and find matching files
"""


class Parser():
    def __init__(self, start_dir, extension='mp3'):
        self.start_dir = start_dir
        self.extension = extension
        self.file_list = []
        self.stats = {'filtered_files': 0, 'total_files': 0, 'directories': 0, 'filtered_size': 0, 'total_size': 0}

    def set_extension_filter(self, extension):
        """
        Set an extension filter so as to only consider files with a particular extension
        :param string extension: File extension
        :return: void
        """
        self.extension = str(extension)

    def populate_file_list(self):
        """
        Recursively populate a list of matching files
        :return: bool
        @todo: Spot the inefficiencies in this method
        """
        for root, dirs, files in os.walk(self.start_dir, topdown=False):

            for name in files:

                found_file_full_path = os.path.join(root, name)
                extension = os.path.splitext(found_file_full_path)[1].replace('.', '')

                # Collect statistics for total file count and file size
                self.stats['total_files'] += 1
                self.stats['total_size'] += os.path.getsize(found_file_full_path) / (1024 * 1024.0)

                # If we find a file with a matching extension
                if str(extension) == str(self.extension):
                    # Append the matched file, to a local property called file_list
                    self.file_list.append(found_file_full_path)

                    # Keep statistics on how many filtered files we found and their total size
                    self.stats['filtered_files'] += 1
                    self.stats['filtered_size'] += os.path.getsize(found_file_full_path) / (1024 * 1024.0)

            # Count the number of directories ( @todo: can we refactor? )
            for dir_item in dirs:
                self.stats['directories'] += 1

        #Collect cumulative stats for the entire found set
        self.stats['total_size'] = "%d Mb" % round(self.stats['total_size'], 2)
        self.stats['filtered_size'] = "%d Mb" % round(self.stats['filtered_size'], 2)

    def get_file_list(self):
        """
        Getter for found file list
        :return: list
        """
        return self.file_list

    def get_stats(self):
        """
        Getter for cumulative file statics
        :return: dict
        """
        return self.stats