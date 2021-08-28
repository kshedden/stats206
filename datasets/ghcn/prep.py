import gzip
import tarfile
import pandas as pd
from io import StringIO
import numpy as np

np.random.seed(34234)

stat = {}
with gzip.open("raw/ghcnd-stations.txt.gz", "rt") as g:
    for line in g:
        idx = line[0:11]
        lat = float(line[12:20])
        lon = float(line[21:30])
        elv = float(line[31:37])
        stat[idx] = [lat, lon, elv]

mtypes = set(["TMAX", "TMIN"])

f = gzip.open("raw/ghcnd_gsn.tar.gz")
t = tarfile.open(fileobj=f)

head = ["id", "year", "month", "day", "lat", "lon", "elev", "mode", "value"]

da = []
for mem in t.getmembers():

    if np.random.randint(5) != 0:
        continue

    if not mem.name.endswith(".dly"):
        continue

    x = t.extractfile(mem)
    y = x.read().decode()

    for z in y.split("\n"):
    
        mt = z[17:21]
        if mt not in mtypes:
            continue
            
        idx = z[0:11]
        if idx not in stat:
            continue

        if stat[idx][2] == -999.9:
            continue

        info = [str(x) for x in stat[idx]]
        year = int(z[11:15])
        month = int(z[15:17])

        q = 21
        for i in range(31):
            v = int(z[q:q+5])
            if z[q + 6] != ' ':
                continue
            if v != -9999:
                q += 8
                row = [idx, year, month, i+1, info[0], info[1], info[2], mt.lower(), v]
                da.append(row)

df = pd.DataFrame(da, columns=head)
df1 = df.loc[df["mode"]=="tmin", :]
df2 = df.loc[df["mode"]=="tmax", :]
ix = ["id", "year", "month", "day", "lat", "lon", "elev"]
dx = pd.merge(df1, df2, left_on=ix, right_on=ix) 

dx = dx.drop(["mode_x", "mode_y"], axis=1)
dx = dx.rename(columns={"value_x": "tmin", "value_y": "tmax"})

dx.tmin /= 10
dx.tmax /= 10

dx["date"] = [pd.datetime(y, m, d) for (y, m, d) in zip(dx.year, dx.month, dx.day)]
dx = dx.drop(["year", "month", "day"], axis=1)

dx = dx.loc[:, ["id", "date", "lat", "lon", "elev", "tmin", "tmax"]]

dx.to_csv("../data/ghcnd_gsn.csv.gz", index=None)
