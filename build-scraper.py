#!/usr/bin/env python
# coding: utf-8

import os
from zipfile import ZipFile
from sh import mkdir, cp, rm

from buildtools import createOrUpdateLambdaLayer

resourceOriginalDirectory1 = "aws_webscraping_layer/lib/python3.6/site-packages/"
resourceOriginalDirectory2 = "aws_webscraping_layer/lib/python3.7/site-packages/"

lambdaLayers = {}
resourceZipDirectories = {}

#Create a lambda layer for web scraping
lambdaLayers['scraping'] = [
    resourceOriginalDirectory1+"bs4", 
    resourceOriginalDirectory1+"selenium", 
    resourceOriginalDirectory2+"bs4",
    resourceOriginalDirectory2+"selenium",
    "bin/webclaw.py"
]
resourceZipDirectories['scraping'] = "python/"

#Create a place to put the resources while zipping them.

layerPublishResponse = []
for name, sources in lambdaLayers.items():
    print("Creating lambda layer for "+name+" with "+str(sources))
    resourceZipDirectory = resourceZipDirectories[name]
    mkdir("-p", resourceZipDirectory)
    for source in sources:
        try:
            cp("-rf", source, resourceZipDirectory)
        except:
            print("No source found at",source)
    with ZipFile(name+".zip", 'w') as ziph:
        for root, dirs, files in os.walk(resourceZipDirectory):
            for file in files:
                ziph.write(os.path.join(root, file))
                
    response = createOrUpdateLambdaLayer(name, name+".zip", runtimes=['python3.6','python3.7'])
    layerPublishResponse.append(response)
    print(response)
    print("Finished creating lambda layer")
    rm("-rf", resourceZipDirectory)
