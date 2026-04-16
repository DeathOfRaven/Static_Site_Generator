from copystatic import recursive_copy
import os
import shutil
from  gencontent import generate_pages_recursive

def main():
    if os.path.exists("./public"):
        shutil.rmtree("./public")
    recursive_copy("./static", "./public")

    generate_pages_recursive("content", "template.html", "public")

main()