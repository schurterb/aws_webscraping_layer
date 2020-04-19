#!/bin/bash

#To simplify dealing with codebuild and codepipeline quirks, this script is executed in the build segment of code build.

echo "project_name="$project_name
source $project_name/bin/activate

sudo apt install zip python3-pip
pip3 install awscli

echo "Compressing bin"
zip -r bin/* layer.zip

echo "Publish lambda layer"
aws lambda publish-layer-version --layer-name "scraping" --compatible-runtimes "python3.6" "python3.7" --zip-file fileb://layer.zip


deactivate