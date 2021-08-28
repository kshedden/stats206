import pandas as pd

demo = pd.read_sas("raw/DEMO_I.XPT")
bmx = pd.read_sas("raw/BMX_I.XPT")
bpx = pd.read_sas("raw/BPX_I.XPT")

demo_vars = ["SEQN", "RIDAGEYR", "RIAGENDR"]
demo = demo[demo_vars]

bmx_vars = ["SEQN", "BMXWT", "BMXHT", "BMXBMI"]
bmx = bmx[bmx_vars]

bpx_vars = ["SEQN", "BPXSY1", "BPXSY2", "BPXSY3"]
bpx = bpx[bpx_vars]

df = pd.merge(demo, bmx, left_on="SEQN", right_on="SEQN")
df = pd.merge(df, bpx, left_on="SEQN", right_on="SEQN")

df.to_csv("../data/nhanes.csv.gz", index=None)