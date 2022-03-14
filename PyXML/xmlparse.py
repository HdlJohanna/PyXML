import json
import re

def ParseXMLElement(code:str, tag):
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
    
    start = code.find(f'<{tag}>') + len(f'<{tag}>')
    end = code.find(f'</{tag}>')
    return code[start:end]

def DictDump(code:str) -> dict:
    """
    Takes XML Code and dumps it into a dictionary

    :param code:str: Used to Pass the code of the xml file
    :return: A Dictionary
    """
    elements = re.findall(r'<[^>]+>', code)
    res = {}
    for el in elements:
        if "/" in el:
            continue
        else:
            res[el.strip("<>")] = ParseXMLElement(code,el.strip("<>"))
    return res
