#!/bin/bash

DIR=$(dirname $0)

$DIR/bin/python3 $DIR/py-do-dyndns/dyndns.py >> $DIR/py-do-dyndns.log 2>&1
