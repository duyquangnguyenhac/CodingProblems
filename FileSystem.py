# This is a variation of design FileSystem
# Implement a file system that support the following functions
# Mkdir
# touch
# ls
# cd
# Cannot have duplicate file names under the same folder


# Brainstorm
#
from collections import defaultdict
class Node:
    def __init__(self, name=""):
        self.name = name
        self.dirs = defaultdict(Node)
        self.files = set()

class FileSystem: 
    def __init__(self):
        self.root_dir = Node("~")
        self.cur_dir = self.root_dir

    # mkdir takes in a path, create a path from root or current position
    def mkdir(self, path):
        path_tokens = path.split("/")
        tmp_pointer = self.cur_dir
        for directory in path_tokens:
            if directory == "":
                continue
            else:
                if directory not in tmp_pointer.dirs:
                    tmp_pointer.dirs[directory] = Node(directory)
                tmp_pointer = tmp_pointer.dirs[directory]
        return 
    
    def touch(self, file_name):
        if file_name not in self.cur_dir.files:
            self.cur_dir.files.add(file_name)
    
    def cd(self, path):
        path_tokens = path.split("/")
        tmp_pointer = self.cur_dir

        for directory in path_tokens:
            if directory == "": continue
            if directory not in tmp_pointer.dirs:
                raise KeyError("Path doesn't exist")
            else:
                tmp_pointer = tmp_pointer.dirs[directory]
        self.cur_dir = tmp_pointer
        return 
    def ls(self):
        return list(self.cur_dir.files)


fs = FileSystem()
fs.mkdir("/dev/machine/")
print(fs)
fs.cd("/dev/machine")
fs.touch("james.txt")
print(fs.ls())
