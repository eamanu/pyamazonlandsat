import attrs
import os
import tarfile

from pyamazonlandsat.utils import get_path_row_from_name
from pyamazonlandsat.downloader import Downloader


class Product:
    name = attrs.ib()
    output_path = attrs.ib()
    _path_files = attrs.ib(init=False)
    _link = attrs.ib(init=False, default='')

    def _generate_link(self):
        path, row = get_path_row_from_name(self.name)
        self._link = 'c1/L8/%s/%s/%s' % (path, row, self.name)

    def _compress_product(self):
        with tarfile.open(
            os.path.join(self.output_path, self.name), 'w') as tar:
            for ff in os.listdir(self._path_files):
                tar.add(
                    os.path.join(
                    self._path_files, ff),
                    ff)

    def get_image_product(self):
        downloader = Downloader(self._link)
        self._path_files = downloader.download_images()
        self._compress_product()
