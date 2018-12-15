#!/bin/sh
brew install pipenv
pipenv --python 2.7.15 install -r requirements.txt
wget https://geolite.maxmind.com/download/geoip/database/GeoLite2-City-CSV.zip
tar xzvf GeoLite2-City.tar.gz
mv GeoLite2-City-CSV/GeoLite2-City-CSV_*/GeoLite2-City-Locations-en.csv .
rm -rf GeoLite2-City-CSV*
python parse.py
#wget https://download.geonames.org/export/dump/timeZones.txt
#wget https://download.geonames.org/export/dump/cities500.zip

