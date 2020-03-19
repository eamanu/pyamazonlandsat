import attrs


@attrs.s
class Service:
    sat = attrs.ib(default='L8')
    collection = attrs.ib(default='c1')
    link = attrs.ib(default='https://landsat-pds.s3.amazonaws.com/')
