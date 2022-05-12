#!/bin/sh

cd ./web-for-twitterati || exit
mate-terminal --tab -- bash -c "../backend/run; bash" && mate-terminal --tab -- bash -c "yarn dev; bash" ; sleep 5; xdg-open http://localhost:3000
wait
