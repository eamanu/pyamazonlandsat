import attrs
import re

from bs4 import BeautifulSoup
from urllib import request
from tempfile import mkdtemp

class Downloader:
    link = attrs.ib()
    _html = attrs.ib(init=False, default='')
    _soup = attrs.ib(init=False, default=None)
    _links_tiff = attrs.ib(init=False, default=list())
    _links_mtl_ang_files = attrs.ib(init=False, default=list())
    _tmp_folder = attrs.ib(init=False default=mkdtemp())

    def __read_key_value(self, pattern):
        for link in self._soup.find_all('a'):
            value = link.get('href')
            if re.match(pattern, value):
                yield value

    def read_link(self):
        self._html = request.urlopen('%s/index.html' % self.link).read()
        self._soup = BeautifulSoup(self._html, 'html.parser')

    def get_download_links_tiff(self):
        self._links_tiff.append(self.__read_key_value('.*.TIF'))

    def get_mtl_ang_files(self):
        self._links_mtl_ang_files.append(self.__read_key_value('.*.txt'))

    def _prepare_for_download(self):
        self.read_link()
        self.get_download_links_tiff()
        self.get_mtl_ang_files()
        return True

    def _save_file_on_tmp_folder(self, name, content):
        with open(os.path.join(self._tmp_folder, name), 'wb') as f:
            f.write(content)

    def _download_file(self, name):
        file_content = requests.get('%s/%s' % (self.link, name),
                                    allow_redirect=True)
        self._save_file_on_tmp_folder(name, file_content)

    def download_images(self):
        self._prepare_for_download()

        for tiff in self._links_tiff:
            self._download_file(tiff)
        for txt in self._links_mtl_ang_files:
            self._download_file(txt)

        return self._tmp_folder
