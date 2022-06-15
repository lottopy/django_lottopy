#!/bin/bash

pgrep nginx
if [ $? -ne 0 ]
then 	
	rc-service nginx start
fi
