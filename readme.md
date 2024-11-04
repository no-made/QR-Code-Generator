This is a simple python script that generates a QR Code image.
1. Create a conda environment with python 3.11
2. install Pillow:
   `conda install conda-forge::pillow`
3. install Qrcode:
    `conda install conda-forge::qrcode`
to use it run the script following this example:

_python QR_Gen.py 'web address' 'output path' --box_size 20 --border 2_

--box_size: Sets the size of each box in the QR code grid. Increasing this value will make the QR code larger.
--border: Sets the thickness of the border around the QR code. Adjusting this helps if you need more or less padding.

Example: 

`python QR_Gen.py "https://micc.unifi.it" "output/QR_MICC.png"` --box_size 20 --border 2