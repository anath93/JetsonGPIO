# Copyright (c) 2019-2023, Jueon Park(pjueon) <bluegbgb@gmail.com>.
# 
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

import os
import shutil
import sys

try:
    print("Collecting the installed files...")
    
    with open("./install_manifest.txt", "r") as f:
        paths = [l.strip() for l in f.readlines() if not l.startswith("/lib/udev")]

    installation_path = os.path.commonprefix(paths)
    destination_path = "./install"
    print(f"Installation path: {installation_path}")

    if not os.path.exists(destination_path):
        os.makedirs(destination_path)

    for input_path in paths:
        filename = os.path.basename(input_path)
        directory = input_path[len(installation_path):-len(filename)]

        directory = os.path.join(destination_path, directory)
        if not os.path.exists(directory):
            os.makedirs(directory)

        output_path = os.path.join(directory, filename)
        shutil.copy(input_path, output_path)

        print(f"Copy '{input_path}' to '{output_path}'")
    
    print("Done.")

except Exception as e:
    print(e)
    sys.exit(1)
