#!/bin/sh

# python backend start up
bash -c ./WebApp/app.py

#react
cd ../web-for-twitterati || exit
yarn start
