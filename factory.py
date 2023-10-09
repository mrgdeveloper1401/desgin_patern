from abc import ABC, abstractmethod


class File(ABC):
    def __init__(self, file):
        self.file = file
        
    @abstractmethod
    def make(self):
        pass
    
    def call_edit(self):
        product = self.make()
        result = product.edit(self.file)
        return result

class JsonFile(File):
    def make(self):
        return Json()


class XmlFile(File):
    def make(self):
        return Xml()
    
class Json:
    def edit(self, file):
        return f'working on {file} json ...'
    

class Xml:
    def edit(self, file):
        return f'working on {file} xml...'
    

class Client:
    def __init__(self, file, file_format):
        self.formats = {
            'json': JsonFile,
            'xml': XmlFile,
        }
        self.result = self.formats[file_format](file)
    
    def call_edit(self):
        return self.result.call_edit()


