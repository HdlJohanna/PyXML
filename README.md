# PyXML
XML Parser for Python

## Quickstart

Let's take this XML File:  
```
<note>
<to>You</to>
<from>Johanna</from>
<heading>Reminder</heading>
<body>Don't forget me this weekend!</body>
</note>
```

Then we can look for Tags using `~.xmlparse.ParseXMLElement` (FindString):  

```py
from PyXML import ParseXMLElement

code = open("sample.xml","r+").read()
heading = ParseXMLElement(code,"heading")
print(heading)
```

## Getting ALL Tags as Dictionary:
```py
from PyXML import DumpDict

code = open("sample.xml","r+").read()
tags = DumpDict(code)
print(tags)
```


Will output:  
`Reminder`  
