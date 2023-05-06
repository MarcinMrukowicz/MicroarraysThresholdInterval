import pandas as pd

datasets = {"colon" : pd.read_excel("RESULTS_COLON_final_v3.xlsx", index_col=0),
            "almall" : pd.read_excel("RESULTS_ALMALL_final_v3.xlsx", index_col=0),
            "dlbcl" : pd.read_excel("RESULTS_DLBCL_final_v3.xlsx", index_col=0),
            "ovarian" : pd.read_excel("RESULTS_ovarian_final_v3.xlsx", index_col=0),
            "prostate" : pd.read_excel("RESULTS_prostate_final_v3.xlsx", index_col=0)}

for dataset_name, dataset in datasets.items():
    print(dataset_name)