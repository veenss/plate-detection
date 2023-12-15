import pandas as pd
import json
import sys
import os

def parse_file(filename):
    df = pd.read_csv(filename)
    df = df.drop(['file_size', 'file_size','file_attributes','region_count','region_id', 'region_attributes'], axis=1)
    StartX = []
    StartY = []
    EndX = []
    EndY = []
    for i in df.index:
        data = json.loads(df['region_shape_attributes'][i])
        StartX.append(data['x'])
        StartY.append(data['y'])
        EndX.append(data['x'] + data['width'])
        EndY.append(data['y'] + data['height'])
    data_dict = {'StartX': StartX, 'StartY': StartY, 'EndX': EndX, 'EndY': EndY}
    df = df.drop(['region_shape_attributes'], axis=1)
    df2 = pd.DataFrame(data_dict)
    newdf = pd.concat([df, df2], axis=1)
    newdf.to_csv('result.csv', index=False)

if __name__ == "__main__":
    # Pastikan argumen file disediakan
    if len(sys.argv) != 2:
        print("Usage: python pengolah.py <filename>")
        sys.exit(1)

    # Ambil nama file dari argumen baris perintah
    file_to_process = sys.argv[1]

    # Periksa apakah file ada
    if not os.path.exists(file_to_process):
        print(f"File '{file_to_process}' not found.")
        sys.exit(1)

    # Proses file
    parse_file(file_to_process)