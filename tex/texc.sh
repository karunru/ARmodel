#!/bin/sh

name=$1

platex "${1%.*}.tex"
dvipdfmx -o "${1%.*}.pdf" "${1%.*}.dvi"

