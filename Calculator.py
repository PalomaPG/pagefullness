# -*- encoding : utf-8 -*-

import os
from os import listdir
from os.path import isfile, join
import resource

class Calculator:

    def __init__(self, path, files_prefix, files_suffix):
        self.file_ = files_prefix+"reg.txt"
        self.files_prefix = files_prefix
        self.files_suffix = files_suffix
        self.path = path


    def sumRatios(self):
        """
        lists files in path which end with a suffix  equals to files_suffix
        and begin with a prefix equals to files_prefix
        :return: sum of fullnes ratio of every file taken in account
        """
        pagesize = resource.getpagesize()

        onlyfiles = [f for f in listdir(self.path) if isfile(join(self.path, f))]

        for file in onlyfiles:
            print(file)
            statinfo = os.stat(self.path+file)
            ratio=statinfo.st_size/pagesize
            print(ratio*100)
    #def calculate(self):



