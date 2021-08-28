#!/bin/bash

curl https://www2.census.gov/programs-surveys/acs/data/pums/2018/1-Year/csv_hus.zip > csv_hus.zip
unzip -o csv_hus.zip

gzip psam_husa.csv
gzip psam_husb.csv
rm csv_hus.zip