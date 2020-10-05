import os
import os.path as p
import pandas as pd
import argparse

psr = argparse.ArgumentParser()
psr.add_argument('input_dir', help='Directory containing images inside folders having names - "land","l_w" or "water"')
args = psr.parse_args()
ld = list(dict())
for dp,dirs,files in os.walk(args.input_dir):
    for nm in files:
        if nm.endswith('.png'):
            lbl = p.split(dp)[-1]
            if lbl in ['land', 'l_w', 'water']:
                ld.append({'img_dir':dp,'img_name':nm,'label':lbl})

df = pd.DataFrame(ld)

df.to_csv('classifier.csv', index=False)

df1 = pd.read_csv('classifier.csv')