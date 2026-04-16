from copystatic import recursive_copy
import os, shutil, sys

from  gencontent import generate_pages_recursive

def main():
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"

    if os.path.exists("./docs"):
        shutil.rmtree("./docs")
    recursive_copy("./static", "./docs")

    generate_pages_recursive("content", "template.html", "docs", basepath)

main()