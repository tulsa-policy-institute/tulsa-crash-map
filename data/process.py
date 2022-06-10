import pandas as pd 
import geopandas as gpd  
import pyarrow.feather as feather
from os.path import exists

def load_data():
    if(exists("wrecks.csv")):
        df = pd.read_csv("wrecks.csv")
        return df

df = load_data()

subset = df[["Type_of_Collision", "Manner_of_Collision", "Num_Pedestrians","Lat", "Long", "Year"]]
subset["Type_of_Collision"] = subset["Type_of_Collision"].astype("category")
subset["Manner_of_Collision"] = subset["Manner_of_Collision"].astype("category")
subset["Num_Pedestrians"] = subset["Num_Pedestrians"].astype("int32")
subset["Lat"] = subset["Lat"].astype("float")
subset["Long"] = subset["Long"].astype("float")
subset["Year"] = subset["Year"].astype("int")

subset.to_csv("subset/wrecks.csv",index=False)

feather.write_feather(subset,"subset/wrecks.arrow")
feather.write_feather(subset,"subset/wrecks.compressed.arrow", compression='zstd')
