Usage
-----

To use you must be know the name of the product to download

And just run the command:

.. code-block:: bash

   $ pys3landsat -n LC08_L1TP_231080_20200128_20200210_01_T1 -o ~/download_products


For information of the parameters you could run `--help`


.. code-block:: bash

   $ pys3landsat --help
   usage: pys3landsat [-h] [-n NAME] [-o OUTPUT]

   Download Landsat 8 images from Amazon S3

   optional arguments:
     -h, --help            show this help message and exit
     -n NAME, --name NAME  Name of the product to download.
     -o OUTPUT, --output OUTPUT
                           Output path to the product.

