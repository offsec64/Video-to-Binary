# Video-to-Binary


## How to use

First, we need to get the script itself. In the Ubuntu shell, type the following command to clone the repository. make sure to be in the directory you want.

`git clone https://github.com/offsec64/video-to-binary/`

Then, go to base64 guru, upload your video file and copy the base64 output.

[base64.guru](https://base64.guru/converter/encode/video)

Then, edit the python file `Base64ToBinary.py` and paste the base64 here:
`t= "BASE64 GOES HERE!".encode("ascii")`

Then run the script and you will now have an output!

> I know this isn't the most elegant solution, but it works!