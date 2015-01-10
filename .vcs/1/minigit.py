#!/usr/bin/env python
# A (re)version control system in python
# Not much in common with git actually...
#

import os
import sys
import shutil
import distutils.dir_util

def backup():
    """
    Makes a copy of the files in the working directory into a .vcs/# directory, starting with 1
    """
    #Copy all the files/directories in the current working directory
    shutil.copytree(os.getcwd(), get_dir(), symlinks=False, ignore=shutil.ignore_patterns(".vcs"))
    
def revert(x):
    """
    Takes a version number as an argument, reverts back to that commit.

    Accomplished by removing all the files+directories in the current working directory (save for .vcs) then copying
    the contents of an earlier commit to the working directory.
    """
    for file in visible_files('.'):
        distutils.dir_util.move_file(os.getcwd(), os.mkdir(get_dir()))
    distutils.dir_util.copy_tree(form_dir(x), os.getcwd(), preserve_mode = 1, preserve_time = 1)

def latest():
    """
    Reverts to the latest version.
    """
    print max(visible_files('.vcs/'))
    try:
        #max([x for file in visible_files('.vcs/')])
        pass
    except:
        print "There are no exisiting backups, first make a backup using 'python minigit.py backup'."     

def get_dir():
    #If the .vcs doesn't already exist, make one then return .vcs/1 
    if ".vcs" not in os.listdir('.'):
        os.mkdir(".vcs")
        return ".vcs/1"
    else:
        x = 1
        while True:
            x += 1
            if str(x) in os.listdir('.vcs'):
                continue
            else:
                return ".vcs/" + str(x)
    
def form_dir(x):
    new_dir = ".vcs/" + str(x)
    return new_dir
    
def visible_files(path):
    """
    Returns a list containing all the files and directories in the current directory (like os.listdir()) which are not hidden (unlike os.listdir())
    """
    filelist = []
    for file in os.listdir(path):
        if not file.startswith('.'):
            filelist.append(file)
    
    return filelist

if __name__ == "__main__":
    #A dictionary which contains a table of the possible functions
    cmd_dict = {'backup':backup, 
                'revert':revert,
                'latest':latest}
      
    #Take the command line argument, check which function is being referenced and call it   
    # * = splat
    cmd_dict[sys.argv[1]](*sys.argv[2:])
    
    