from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED = "unordered_list"
    ORDERED = "ordered_list"

def block_to_block_type(text):
    # heading
    headings = ["# ", "## ", "### ", "#### ", "##### ", "###### "]
    check = False
    for heading in headings:
        if text.startswith(heading):
            check = True
            break
    if check == True:
        return BlockType.HEADING
    
    #Code Block
    lines = text.split("\n")
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    
    #Quote
    check = True
    for line in lines:
        if not line.startswith(">"):
            check = False
            break
    if check == True:
        return BlockType.QUOTE

    #Unordered List
    check = True
    for line in lines:
        if not line.startswith("- "):
            check = False
            break
    if check == True:
        return BlockType.UNORDERED
    
    #ordered List
    check = True
    count = 1
    for line in lines:
        if not line.startswith(f"{count}. "):
            check = False
            break
        count += 1
    if  check == True:
        return BlockType.ORDERED
    
    #Paragraph
    return  BlockType.PARAGRAPH