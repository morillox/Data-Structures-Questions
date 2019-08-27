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
    main_dir = os.listdir(path)
    inner_dirs = [obj for obj in main_dir if os.path.isdir(path+"/"+obj)]
    inner_files = [obj for obj in main_dir if os.path.isfile(path+"/"+obj)]

    matching_files = [path+"/"+ file for file in inner_files if file.endswith(suffix)]
    for dir in inner_dirs:
        matching_files += find_files(suffix, path+"/"+dir)
    return matching_files


print(find_files(".c", 'testdir'))
print(find_files(".c", '.'))
print(find_files('.c', 'testdir/subdir3'))
print(find_files('aaa','testdir'))
