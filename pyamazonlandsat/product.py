import attrs


class Product:
    nombre = attrs.ib()
    _path_files = attrs.ib(init=False)

    def _compress_product(self):
        pass

    def get_image_product(self, name):
        pass


