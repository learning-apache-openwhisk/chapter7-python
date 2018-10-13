#!/bin/sh
if test -d virtualenv
then echo "use source virtualenv/bin/activate" ; exit
fi
virtualenv virtualenv  --python python3
source virtualenv/bin/activate
pip install -r requirements3.txt
pip install httpretty

