#!/bin/bash

DIR=$(dirname $0)
source $DIR/bin/activate

$DIR/py-do-dyndns/dyndns.py >> $DIR/py-do-dyndns.log
