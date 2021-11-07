#!/bin/bash

echo Warning: running this script will overwrite your existing notebooks for Statistics 206.
echo Exit now by typing ctrl-c to prevent this from happening.
echo Press any other key to continue.
read

nb=(scooters_basic acs_basic acs_graphing who_mort nhanes_basic ghcn_basic ohie_basic)

for v in ${nb[@]}; do 
    wget raw.githubusercontent.com/kshedden/stats206/main/case_studies/${v}.ipynb -O ${v}.ipynb
done

