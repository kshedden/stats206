"""
Generate smaller versions of the Austin scooter data. 
"""

import csv
import gzip
import numpy as np

ids = set([])

with gzip.open("raw/austin_emobility.csv.gz", "rt") as f:
    r = csv.reader(f)
    head = next(r)
    for row in r:
        if row[2] == "scooter":

            # Skip rows with missing values
            k = True
            for j in 11, 12, 14, 15:
                try:
                    float(row[j])
                except ValueError:
                    k = False
            if not k:
                continue

            ids.add(row[1])

ids = list(ids)
ids_short = np.random.choice(ids, 20000, replace=False)
ids_short = set(ids_short)
ids_tiny = np.random.choice(ids, 4000, replace=False)
ids_tiny = set(ids_tiny)

with gzip.open("raw/austin_emobility.csv.gz", "rt") as f,\
     gzip.open("../data/scooters_short.csv.gz", "wt") as g,\
     gzip.open("../data/scooters_tiny.csv.gz", "wt") as h:
    r = csv.reader(f)
    wg = csv.writer(g)
    wh = csv.writer(h)
    head = next(r)
    wg.writerow(head[1:])
    wh.writerow(head[1:])

    for row in r:

        # Skip rows with missing values
        k = True
        for j in 11, 12, 14, 15:
            try:
                float(row[j])
            except ValueError:
                k = False
        if not k:
            continue

        if row[1] in ids_short:
            wg.writerow(row[1:])
        if row[1] in ids_tiny:
            wh.writerow(row[1:])
