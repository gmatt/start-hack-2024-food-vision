import os

import pandas as pd
from pyprojroot import here

df = pd.read_csv(
    here("../data/nutrition5k/nutrition5k_dataset-metadata-dish_metadata_cafe1.csv"),
    low_memory=False,
    on_bad_lines="skip",
)

df = df[:100]


for i, row in df.iterrows():
    os.system(
        f"gsutil -m cp -r gs://nutrition5k_dataset/nutrition5k_dataset/imagery/realsense_overhead/{row.iloc[0]}/rgb.png {here('../data/nutrition5k/') / (row.iloc[0] + '.png')}"
    )
