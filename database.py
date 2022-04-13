import sys
import xml.sax
from pymongo import MongoClient

file_name = r"D:\Downloads\catalog.rdf\catalog.rdf"


class Book:
    id = None
    title = None
    friendly_title = None
    author = None
    language = None
    downloads = None
    
    def __init__(self, bid):
        self.id = bid
    
    def to_dict(self):
        d = {
            "id": self.id,
        }
        if self.title is not None:
            d["title"] = self.title
        if self.friendly_title is not None:
            d["friendly_title"] = self.friendly_title
        if self.author is not None:
            d["author"] = self.author
        if self.language is not None:
            d["language"] = self.language
        if self.downloads is not None:
            d["downloads"] = self.downloads
        return d
        
    def __str__(self):
        s = "Book ID: " + self.id + "\n"
        if self.title is not None:
            s += " Title: " + self.title + "\n"
        if self.friendly_title is not None:
            s += " Friendly Title: " + self.friendly_title + "\n"
        if self.author is not None:
            s += " Author: " + self.author + "\n"
        if self.language is not None:
            s += " Language: " + self.language + "\n"
        if self.downloads is not None:
            s += " Downloads: " + str(self.downloads) + "\n"
            
        return s


class GutenburgHandler(xml.sax.ContentHandler):
    
    count = 0
    book = None
    collection = None
    
    def __init__(self, collection, exit_limit=0):
        self.collection = collection
        self._charBuffer = []
        self.in_book = False
        
        if exit_limit > 0 :
            self.limit = exit_limit

    def commit(self):
        self.collection.insert_one(self.book.to_dict())

    def _getCharacterData(self):
        s = ''.join(self._charBuffer)
        self._clearCharaterData()
        return s.strip()
    
    def _clearCharaterData(self):
        self._charBuffer = []
    
    def characters(self, data):
        self._charBuffer.append(data)
    
    def startElement(self, name, attrs):

        if self.count > self.limit :
            print( "Limit reached, exiting" )
            sys.exit(0)
            
        if name == "pgterms:etext":
            self.in_book = True

        if not self.in_book :
            return

        if name == "pgterms:etext":
            bid = attrs.getValue("rdf:ID").replace("etext", "")
            self.book = Book( bid )
            self.count += 1
    
        if name in [
            "dc:title",
            "pgterms:friendlytitle",
            "dc:language",
            "pgterms:downloads",
            "dc:creator"
        ]:
            self._clearCharaterData()
        
    def endElement(self, name ):
        
        if name == "pgterms:etext" :
            self.in_book = False
            self.commit()
    
        if not self.in_book :
            return
        
        if name == "dc:title":
            title = self._getCharacterData()
            self.book.title = title
            
        if name == "pgterms:friendlytitle":
            friendly_title = self._getCharacterData()
            self.book.friendly_title = friendly_title
            
        if name == "dc:creator":
            author = self._getCharacterData()
            self.book.author = author
                
        if name == "dc:language" :
            language = self._getCharacterData()
            self.book.language = language
            
        if name == "pgterms:downloads" :
            downloads = self._getCharacterData()
            try:
                self.book.downloads = int(downloads)
            except:
                pass


client = MongoClient()
db = client["gutenburg"]
collection = db["books"]

parser = xml.sax.make_parser()
parser.setContentHandler(GutenburgHandler(collection, 10))
parser.parse( open(file_name, "r", encoding="utf-8") )