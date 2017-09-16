#!/bin/bash

DIRECTORY='/home/michael/.devilspie/'
ONFILE='all-deco-on.dsx'
OFFFILE='all-deco-off.dsx'
ACTIVEFILE='deco.ds'

CURRENT="$(readlink $DIRECTORY$ACTIVEFILE)"
 rm -f "$DIRECTORY$ACTIVEFILE"
if [ "$CURRENT" == "$DIRECTORY$ONFILE" ]; then
	ln -s "$DIRECTORY$OFFFILE" "$DIRECTORY$ACTIVEFILE"
	echo "turn off"
else
	echo "turn on"
	#echo "$CURRENT"
	#echo "$ONFILE"
	ln -s "$DIRECTORY$ONFILE" "$DIRECTORY$ACTIVEFILE"
fi

pkill devilspie; devilspie -a &
