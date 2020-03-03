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
    if (suffix == "" ) and (path == ""):
        print("suffix and path are empty.")
        return plist
    elif suffix == "" :
        print("suffix is empty.")
        return plist
    elif path == "":
        print("path is empty.")
        return plist

    if os.path.isfile(path):
        if path.endswith(suffix):
            plist.append(path)
        return plist




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
if __name__ == "__main__":
    print(find_files('.c', './testdir'))
    print(find_files('.h', './testdir'))
    print(find_files('.cpp', './testdir'))#empty
    print(find_files('.gitkeep', './testdir'))


    print(find_files('.c', './testdir/t1.c')) #
    print(find_files('.c', './testdir/t1.h'))# empty

    print(find_files('', '')) # empty
    print(find_files('', './testdir/t1.h')) # empty
    print(find_files('.c', '')) # empty