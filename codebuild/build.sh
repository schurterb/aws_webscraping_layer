#!/bin/bash

#To simplify dealing with codebuild and codepipeline quirks, this script is executed in the build segment of code build.

echo "project_name="$project_name
source $project_name/bin/activate

echo " ---------------------- "
echo "python3 build-scraper.py"
python3 build-scraper.py
echo " ---------------------- "

deactivate