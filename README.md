Function:
Encode data inside of a JPG, then base64 the blob, then zlib the blob
Decode the data inside of said blob

How it works without modifying the data:
The ending footer of a .jpg file is FF D9. In the RFC / standards of a JPG, all programs read until the end of it, and render the jpg accordingly. So you could add "my pink pony rides rainbows" to the end of a JPG after the FF D9...and everything is good.

How the code works:
a 6-byte sanity check is performed, looking for the 6 bytes of "\xd9\xff\x24\x42\x00\x00" in a JPG. If found, it starts decoding the blob, -2 bytes

How to encode:
python imageEncode.py e hitch.jpg output.jpg "This is a test. woot"

How to decode:

python imageEncode.py d output.jpg
