#!/bin/sh

# python backend start up
bash -c ./backend/app.py

#react
cd ./web-for-twitterati || exit
yarn install
yarn start
