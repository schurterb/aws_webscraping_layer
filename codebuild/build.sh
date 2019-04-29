#!/bin/bash

#To simplify dealing with codebuild and codepipeline quirks, this script is executed in the build segment of code build.

echo "project_name="$project_name
source $project_name/bin/activate


echo "Test script to see if it is even possible"

cd scraper
zip -r scraper/document_scraper.py.zip .
cd ..

echo "Finish test script"


echo "Building scraper"
#python3 build-scraper.py
echo "Finished building scraper"

echo "Building webpage"
#python3 build-webpage.py
echo "Finished building webpage"

deactivate