import attrs


class Product:
    nombre = attrs.ib()
    path_files = attrs.ib()

    def compress_product(self):
        pass

