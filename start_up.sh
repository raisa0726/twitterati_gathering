#!/bin/sh

cd ./web-for-twitterati || exit
mate-terminal --tab -- bash -c "../backend/run; bash" && mate-terminal --tab -- bash -c "yarn dev; bash"
