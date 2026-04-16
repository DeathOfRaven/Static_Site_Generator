import os
import shutil

def recursive_copy(src, dst):

    if not os.path.exists(dst):
        os.mkdir(dst)

    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dst_path = os.path.join(dst, item)

        if os.path.isfile(src_path):
            shutil.copy(src_path, dst_path)
            print(f"src: {src_path}, dst: {dst_path}")
        else:
            recursive_copy(src_path, dst_path)