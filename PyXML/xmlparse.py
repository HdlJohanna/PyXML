import json


def ParseXMLElement(code:str,tag):
    """
    The ParseXMLElement function parses a given XML element from the code.
       It takes two arguments: 
           1) The code to be parsed, and 
           2) The tag of the XML element to be parsed.
    
       It returns a string containing the text within that particular XML element.
    
    :param code:str: Used to Pass the code of the xml file.
    :param tag: Used to Specify the tag that is used to identify the start and end of a particular element.
    :return: A tuple containing the string between two xml tags.    
    """
    
    start = code.find(f'<{tag}>')+len(f'<{tag}>')
    end = code.find(f'</{tag}>')
    return code[start:end]

def find(fp,Element,raise_error=False):
    if not Element in fp.read():
        if raise_error:
            raise ValueError(f"Element {Element} is not in File")
        else:
            return -1
    return ParseXMLElement(fp.read(),Element)

def finds(s:str,element,raise_error=False):
    
    if not element in s:
        if raise_error:
            raise ValueError(f"Element {element} is not in Code")
        else:
            return -1
    return ParseXMLElement(s,element)

