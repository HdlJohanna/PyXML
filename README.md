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

Then we can look for Tags using `~.xmlparse.finds` (FindString):  

```py
from PyXML import finds

code = open("sample.xml","r+").read()
heading = finds(code,"heading")
print(heading)
```
Will output:  
`Reminder`  
