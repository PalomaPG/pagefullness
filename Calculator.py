# -*- encoding : utf-8 -*-

from os import stat
from os import listdir
from os.path import isfile, join

import resource
import statistics as sts

class Calculator:

    def __init__(self, path, files_suffix, output_path):
        self.files_suffix = files_suffix
        self.path = path
        self.output_path=output_path


    def writeCalc(self):
        """
        lists files in path which end with a suffix  equals to files_suffix
        and begin with a prefix equals to files_prefix
        :return: sum of fullnes ratio of every file taken in account
        """
        reg = []
        pagesize = resource.getpagesize()

        onlyfiles = [f for f in listdir(self.path) if isfile(join(self.path, f))]

        for file in onlyfiles:
            statinfo = stat(self.path+file)
            ratio=(statinfo.st_size/pagesize)
            reg.append(ratio*100)

        with open(self.output_path, "a") as f:
            f.write('%d,%f,%f\n' % (len(reg), sts.mean(reg), sts.stdev(reg)))

    #def calculate(self):



