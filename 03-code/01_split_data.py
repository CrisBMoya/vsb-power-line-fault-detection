import pyarrow.parquet as pq
import pandas as pd

for i in range(8711):
    print(i)
    col_x = pq.read_pandas("D:/Documentos/raw-data/vsb-power-line-fault-detection/train.parquet", columns=[str(i)]).to_pandas()
    col_x.to_csv(f"D:/Documentos/raw-data/vsb-power-line-fault-detection/train_data/{str(i)}.csv")

