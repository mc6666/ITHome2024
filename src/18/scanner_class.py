import requests

class Scanner:
    def __init__(self, scanner_url):
        self.scanner_url = scanner_url
        
    def scan(self):
        response = requests.get(self.scanner_url)
        self.barcode = response.text