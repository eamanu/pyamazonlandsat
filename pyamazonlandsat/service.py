import attr

from pyamazonlandsat.product import Product


@attr.s
class Service:
    name = attr.ib()
    output_path = attr.ib()

    def get_product(self):
        product = Product(self.name, self.output_path)
        product.get_image_product()

