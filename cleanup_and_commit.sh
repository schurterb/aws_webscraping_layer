#!/bin/bash

#clean up stuff we don't want to commit'
. cleanup_virtual_env.sh $1
rm -rf python
rm -rf __pycache__ *pyc
rm -f *zip
rm -f *log bin/*log
rm -rf bin/locales

#Only commit changes if there is a comment to commit with
git add * -A
if [ "$#" -ne 1 ]
then
  git commit -m "$2"
elif [ "$#" -ne 0 ]
then
  git commit -m "$1"
else
  git commit -m "No comment"
fi
git push