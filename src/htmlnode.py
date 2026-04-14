class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplemented
    
    def props_to_html(self):
        if not self.props:
            return ""
        parts = []
        for key, value in self.props.items():
            parts.append(f'{key}="{value}"')
        return " " + " ".join(parts) 
    
    def __repr__(self):
        return (
            f"Tag= {self.tag}, Value= {self.value},"
            f"Children= {self.children}, Props= {self.props}"
            )

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if not self.value:
            raise ValueError
        if not self.tag:
            return self.value
        
        attrs = self.props_to_html()
        return f"<{self.tag}{attrs}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return (
            f"Tag= {self.tag}, Value= {self.value},"
            f"Props= {self.props}"
            )

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if not self.tag:
            raise ValueError("no tag")
        if not self.children:
            raise ValueError("no child")
        
        children_html = ""
        for child in self.children:
            children_html += child.to_html()
        
        html = self.props_to_html()
        return f"<{self.tag}{html}>{children_html}</{self.tag}>"