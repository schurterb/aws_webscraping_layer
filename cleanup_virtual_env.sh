#!/bin/bash

if [ "$#" -ne 0 ]
then
   project_name=$1
else
   project_name=aws_webscraping_layer
fi

rm -rf $project_name