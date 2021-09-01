#!/usr/bin/env python
import os
import subprocess
from multiprocessing import Pool

src = os.path.expanduser("~/data/prod/")
dest = os.path.expanduser("~/data/prod_backup/")
print("src:{}, dest:{}".format(src, dest))

def get_pathlist(folder):
    walklist = []
    # atuple = (root, dirs, files)
    for atuple in os.walk(folder, topdown=True):
      walklist.append(atuple)
    #print("foler:{}".format(folder))
    #print("walklist:{}".format(walklist))

    # return sub-dir-list at the top level
    return walklist[0][1]

def run(dir):
    print("Handling {}".format(dir))
    src_path = src + dir + "/"
    print("src_path:{}".format(src_path))
    dest_path = dest + dir + "/"
    print("dest_path:{}".format(dest_path))
    subprocess.call(["rsync", "-arq", src_path, dest_path])  

if __name__ == "__main__":
    src_pathlist = get_pathlist(src)
    print("src_pathlist:{}".format(src_pathlist))
    # Create a pool of specific number of CPUs
    p = Pool(len(src_pathlist))
    # Start each task within the pool	
    p.map(run, src_pathlist)
