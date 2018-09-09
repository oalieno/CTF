#!/bin/bash

ffmpeg -i Marcode.mp4 -qscale:v 1 keyframes/frame%06d.jpg
