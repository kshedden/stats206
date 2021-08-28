#!/bin/bash

nb=(scooters_basic acs_basic who_mort nhanes_sampling ghcn_scatterplot)

for v in ${nb[@]}; do 
    wget raw.githubusercontent.com/kshedden/stats206/main/case_studies/${v}.ipynb
done

