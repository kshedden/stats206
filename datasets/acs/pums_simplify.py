import csv
import gzip
from os import path
import numpy as np

keep = ["DIVISION", "PUMA", "REGION", "ST", "NP", "MRGP", "RNTP", "TEN", "VALP", "VEH", "YBL", 
        "FES", "FINCP", "FPARC", "HHT", "HINCP", "HUPAC", "MV", "NOC", "NPF", "NR", "NRC", "PARTNER",
        "R18", "R60", "R65", "TAXAMT", "WIF", "WKEXREL", "WORKSTAT", "FFINCP"]

np.random.seed(893247)

out = gzip.open("../data/pums_short.csv.gz", "wt")
cw = csv.writer(out)

for fx in "ab":

    fn = path.join("raw", "psam_hus%s.csv.gz" % fx)
    with gzip.open(fn, "rt") as f:
        cr = csv.reader(f)
        head = next(cr)
        headix = {v:k for k, v in enumerate(head)}
        itype = headix["TYPE"]
        ii = [headix[v] for v in keep]

        if fx == "a":
            cw.writerow([head[i] for i in ii])
            
        for row in cr:

            # Skip institutional quarters
            if row[itype] != "1":
                continue
        
            if np.random.randint(0, 5) == 0:
                cw.writerow([row[i] for i in ii])

out.close()