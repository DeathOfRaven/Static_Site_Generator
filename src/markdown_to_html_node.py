from htmlnode import ParentNode, HTMLNode
from textnode import text_node_to_html_node, TextNode, TextType
from block import block_to_block_type, BlockType
from convert import text_to_textnodes, markdown_to_blocks

# Helper Functions
def text_to_children(text):
    nodes = text_to_textnodes(text)
    result = []
    for node in nodes:
        result.append(node.text_to_textnodes(node))
    return result

def text_cleaner(text, type):
    lines = text.split("\n")
    cleaned_lines = []
    for line in lines:
        if type == "quote":
            cleaned_lines.append(line[2:])
        if type == "unordered":
            pass
        if type == "ordered":
            pass
        if type == "code":
            pass
        if type == "paragraph":
            pass
        if type == "heading":
            pass
    cleaned = " ".join(cleaned_lines)


def helper_quote(block):
    lines = block.split("\n")
    cleaned_lines = []
    for line in lines:
        cleaned_lines.append(line[2:])
    text = " ".join(cleaned_lines)
    children = text_to_children(text)
    quote_node = ParentNode("blockquote", children)
    return quote_node

def helper_headings(block):
    tag = 0
    for char in block:
        if char == "#":
            tag += 1
        else:
            break
    children  = text_to_children(block[tag + 1:])
    heading_node = ParentNode(f"h{tag}", children)
    return heading_node

def helper_code(block):
    text = block[4: -3]
    inner_node = TextNode(text, TextType.TEXT)
    converted = text_node_to_html_node(inner_node)
    code_node = ParentNode("code", [converted])
    pre_node  = ParentNode("pre", [code_node])
    return pre_node

def helper_unordered(block):
    lines = block.split("\n")
    cleaned_lines = []
    for line in lines:
        temp = line[2:]
        children = text_to_children(temp)
        cleaned_lines.append(ParentNode("li", children))
    return ParentNode("ul", cleaned_lines)
    

def helper_ordered(block):
    lines = block.split("\n")
    cleaned_lines = []
    for line in lines:
        temp = line.split(". ", 1)
        children = text_to_children(temp[1])
        cleaned_lines.append(ParentNode("li", children))
    return ParentNode("ol", cleaned_lines)


def helper_paragraphs(block):
    lines = block.split("\n")
    text = " ".join(lines)
    children = text_to_children(text)
    return ParentNode("p", children)
    
def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    result = []
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.HEADING:
            result.append(helper_headings(block))
        if block_type == BlockType.QUOTE:
            result.append(helper_quote(block))
        if block_type == BlockType.CODE:
            result.append(helper_code(block))
        if block_type == BlockType.ORDERED:
            result.append(helper_ordered(block))
        if block_type == BlockType.UNORDERED:
            result.append(helper_unordered(block))
        if block_type == BlockType.PARAGRAPH:
            result.append(helper_paragraphs(block))
    return ParentNode("div", result)

