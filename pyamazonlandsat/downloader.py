import attrs
import re

from bs4 import BeautifulSoup
from urllib import request

class Downloader:
    link = attrs.ib()
    _html = attrs.ib(init=False, default='')
    _soup = attrs.ib(init=False, default=None)
    _links_tiff = attrs.ib(init=False, default=list())
    _links_mtl_ang_files = attrs.ib(init=False, default=list())

    def read_key_value(self, pattern):
        for link in self._soup.find_all('a'):
            value = link.get('href')
            if re.match(pattern, value):
                yield value

    def read_link(self):
        self._html = request.urlopen(self.link).read()
        self._soup = BeautifulSoup(self._html, 'html.parser')

    def get_download_links_tiff(self):
        self._links_tiff.append(self.read_key_value('.*.TIF'))

    def get_mtl_ang_files(self):
        self._links_mtl_ang_files.append(self.read_key_value('.*.txt'))

    def download_image(self):
        pass



