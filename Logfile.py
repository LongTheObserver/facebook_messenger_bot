import os.path
from os.path import expanduser


class Logfile:

    def __init__(self, file_name):
        self.name = file_name

    def create_file(self):
        home = expanduser("~")
        save_path = home + "/willy"
        file = os.path.join(save_path, self.name + ".txt")
        file1 = open(file, "a")
        return file1

    def record_log(self, content):
        file_2 = self.create_file()
        file_2.write(content)
        file_2.close()
        return file_2

