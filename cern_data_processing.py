import uproot
import pandas as pd
import numpy as np
from pythonosc import udp_client
import time
import random


#file = uproot.open("data/B2HHH_MagnetDown.root")  # Ersetze mit deinemCERN-Datensatz
file = uproot.open("data/PhaseSpaceSimulation.root")  # Ersetze mit deinemCERN-Datensatz
keys = file.keys();
print(keys);
tree = file[keys[0]] 

df = tree.arrays(library="pd")
smallDF = df.head(10000).copy();

#kaon momentum magnitude: p^2=p2x+p2y+p2z
smallDF['H1_P'] = np.sqrt(smallDF['H1_PX']**2 + smallDF['H1_PY']**2 + smallDF['H1_PZ']**2)
smallDF['H2_P'] = np.sqrt(smallDF['H2_PX']**2 + smallDF['H2_PY']**2 + smallDF['H1_PZ']**2)
smallDF['H3_P'] = np.sqrt(smallDF['H3_PX']**2 + smallDF['H3_PY']**2 + smallDF['H1_PZ']**2)

#kaon energy: E^2=p^2+m^2
#kaon invariant mass = 493.677 MeV/c^2

smallDF['H1_E'] = np.sqrt(smallDF['H1_P'] ** 2 + 493.477**2)
smallDF['H2_E'] = np.sqrt(smallDF['H2_P'] ** 2 + 493.477**2)
smallDF['H3_E'] = np.sqrt(smallDF['H3_P'] ** 2 + 493.477**2)


smallDF['B_E'] = smallDF['H1_E'] + smallDF['H2_E'] + smallDF['H3_E']
smallDF['B_PX'] = smallDF['H1_PX'] + smallDF['H2_PX'] + smallDF['H3_PX']
smallDF['B_PY'] = smallDF['H1_PY'] + smallDF['H2_PY'] + smallDF['H3_PY']
smallDF['B_PZ'] = smallDF['H1_PZ'] + smallDF['H2_PZ'] + smallDF['H3_PZ']
smallDF['B_P'] = np.sqrt(smallDF['B_PX']**2 + smallDF['B_PY']**2 + smallDF['B_PZ']**2)

smallDF['B_ChargePositive'] = (smallDF[['H1_Charge','H2_Charge','H3_Charge']] == 1).sum(axis=1) == 2;
smallDF['B_Charge'] = np.where(smallDF['B_ChargePositive'], 1, -1)

preselectedDF = smallDF.loc[(smallDF['H3_ProbPi'] < 0.5) & (smallDF['H2_ProbPi'] < 0.5) & (smallDF['H1_ProbPi'] < 0.5) & (smallDF['H1_ProbK'] > 0.5) & (smallDF['H2_ProbK'] > 0.5) & (smallDF['H3_ProbK'] > 0.5) & (smallDF['H1_isMuon'] == 0) & (smallDF['H2_isMuon'] == 0) & (smallDF['H3_isMuon'] == 0)]

smallerDF= smallDF.head(300).copy()
df_combined = pd.concat([smallerDF, preselectedDF], ignore_index = True)
df_shuffled = df_combined.sample(frac=1).reset_index(drop=True)
print(df_shuffled)


client = udp_client.SimpleUDPClient("127.0.0.1", 7400)  # Max/MSP oder SuperCollider

#for _, row in smallDF.iterrows():
for _, row in df_shuffled.iterrows():
    client.send_message("/antimatter", [ 
    									row["H1_PX"], row["H1_PY"], row["H1_PZ"],
    									row["H2_PX"], row["H2_PY"], row["H2_PZ"],
    									row["H3_PX"], row["H3_PY"], row["H3_PZ"],
    									row["H1_P"], row["H2_P"], row["H3_P"],
    									row["H1_Charge"], row["H2_Charge"], row["H3_Charge"],
    									row["H1_E"], row["H2_E"], row["H3_E"],
    									row["B_FlightDistance"],
    									row["B_PX"], row["B_PY"], row["B_PZ"],
    									row["B_P"], row["B_E"], row["B_Charge"],
                                        row["H1_ProbK"], row["H2_ProbK"], row["H3_ProbK"],
                                        row["H1_ProbPi"], row["H2_ProbPi"], row["H3_ProbPi"],
                                        row["H1_isMuon"], row["H2_isMuon"], row["H3_isMuon"]
    									])
    time.sleep(random.uniform(0.2, 1.0))  # Wartezeit zwischen den Events
#    time.sleep(0.3)  # Wartezeit zwischen den Events


print("Fertig!")