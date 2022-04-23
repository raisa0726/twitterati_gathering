#!/bin/sh

# python backend start up
cd WebApp
bash -c ./app.py

#react
cd ../web-for-twitterati || exit
yarn start
