#!/bin/bash

binwalk -e 0.zlib
mv _0.zlib.extracted/0.zlib ./1.zlib
rm -rf _0.zlib.extracted
