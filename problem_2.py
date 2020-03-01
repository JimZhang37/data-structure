import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """

    plist = []
    currentpath = os.listdir(path)

    for i in currentpath:
        i = path + '/' + i

        if os.path.isfile(i):

            if i.endswith(suffix):

                plist.append(i)
        elif os.path.isdir(i):
            currentlist = find_files(suffix, i)
            plist += currentlist

    return plist

print(find_files('.c', './testdir'))
print(find_files('.h', './testdir'))
print(find_files('.cpp', './testdir'))
print(find_files('.gitkeep', './testdir'))
