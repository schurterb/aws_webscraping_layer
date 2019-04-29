#!/usr/bin/env python
# coding: utf-8

import os
from zipfile import ZipFile
from sh import mkdir, cp, rm

from buildtools import createOrUpdateLambdaLayer

resourceOriginalDirectory = "aws_webscraping_layer/lib/python3.6/site-packages/"

lambdaLayers = {}
resourceZipDirectories = {}

#Create a lambda layer for web scraping
lambdaLayers['scraping'] = [resourceOriginalDirectory+"bs4", resourceOriginalDirectory+"selenium"]
resourceZipDirectories['scraping'] = "python/"

#Create a place to put the resources while zipping them.

layerPublishResponse = []
for name, sources in lambdaLayers.items():
    print("Creating lambda layer for "+name+" with "+str(sources))
    resourceZipDirectory = resourceZipDirectories[name]
    mkdir("-p", resourceZipDirectory)
    for source in sources:
        cp("-rf", source, resourceZipDirectory)
    with ZipFile(name+".zip", 'w') as ziph:
        for root, dirs, files in os.walk(resourceZipDirectory):
            for file in files:
                ziph.write(os.path.join(root, file))
                
    response = createOrUpdateLambdaLayer(name, name+".zip", runtimes=['python3.6','python3.7'])
    layerPublishResponse.append(response)
    print(response)
    print("Finished creating lambda layer")
    rm("-rf", resourceZipDirectory)
