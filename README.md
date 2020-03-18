# animedownloaders
python scripts to download anime

All this script does is save said lyrics to a file

aldl [-h] -s SONG [-a ARTIST] [-l {english,en,japanese,jp}] -T

-h:
	Shows help
-s:
	What song to search
-a:
	Optional, search song with artist
-l:
	Changes langyage song is svaed in.
	Availabe languages.

	- english,en
	-japanese,jp
-T:
	Save title in lyrics

## Installation

### Prerequisites

Install animelyrics by colorfusion
([https://github.com/colorfusion/animelyrics/])

```pip install animelyrics
```

### On Windows

Use command

```python aldl.py
```

to execute

OR

use py2exe to convert the .py file to .exe,
then move it to somewhere in your PATH

### On Linux

execute ```install.py```

OR

```chmod 755 aldl.py
```
```sudo cp aldl.py /usr/bin/aldl
```


# This repo's license

Refer to LICENSE.md

# animelyrics's License


Copyright (c) 2019 Melvin Yeo

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

