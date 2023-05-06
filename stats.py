import pandas as pd
import re
datasets = {
    "colon" : pd.read_excel("RESULTS_COLON_final_v3.xlsx", index_col=0),
            # "almall" : pd.read_excel("RESULTS_ALMALL_final_v3.xlsx", index_col=0),
            # "dlbcl" : pd.read_excel("RESULTS_DLBCL_final_v3.xlsx", index_col=0),
            # "ovarian" : pd.read_excel("RESULTS_ovarian_final_v3.xlsx", index_col=0),
            # "prostate" : pd.read_excel("RESULTS_prostate_final_v3.xlsx", index_col=0)
}

for dataset_name, dataset in datasets.items():
    # Shorten names in aggregation column
    for val in dataset.itertuples():
        match = re.search(r"aggregations\.(.*?)Aggregation", val[1]) # fing string between aggregations. and Aggregation
        if match:
            dataset.at[val[0], 'algorithm'] = "UEA(aggregation="+match.group(1)+")" # replace value in cell
    print(dataset.to_latex())
    print(dataset_name)