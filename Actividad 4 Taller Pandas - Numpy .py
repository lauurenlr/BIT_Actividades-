import pandas as pd
import numpy as np
import matplotlib.pyplot as mat

# Including Dataset from the PC
CO2_Emission_Data= pd.read_csv("C:\\Users\\Usuario\\Desktop\\BIT\\Boot camp\\Clases\\CO2_emission_by_countries_MODIFICADO.csv",encoding = 'latin1')
print(CO2_Emission_Data.head()) #Information of 5 first rows
print("____________________________________________________________________________________")
print(CO2_Emission_Data.info) #Information of Dataset
print("____________________________________________________________________________________")
print(CO2_Emission_Data.describe()) #Showing the summary about the statistical datas
print(CO2_Emission_Data.columns)
print("____________________________________________________________________________________")
#Delete rows with missing data
CO2_Emission_Data = CO2_Emission_Data.dropna(subset=["CO2 emission (Tons)","Year"])
#Making sure the variable Year is whole number
CO2_Emission_Data ["Year"] = CO2_Emission_Data["Year"].astype(int)
print("____________________________________________________________________________________")
print("What countries reduced its CO2 emission between 1990 to 2020?")

#Filtering the information about the CO2 emissions for to years 1990 and 2020
Info_1990 = CO2_Emission_Data[(CO2_Emission_Data["CO2 emission (Tons)"] > 0) & (CO2_Emission_Data["Year"] == 1990)]
Info_2020 = CO2_Emission_Data[(CO2_Emission_Data["CO2 emission (Tons)"] > 0) & (CO2_Emission_Data["Year"] == 2020)]
#For the filtered columns, rename "ï»¿Country" for to "Country"  and "CO2 emission (Tons)" for to "Emissions ((1990 ^ 2020) (Ton))"
Emission_1990 = Info_1990[["ï»¿Country", "CO2 emission (Tons)"]].rename(columns ={"CO2 emission (Tons)": "Emissions 1990 (Ton)", "ï»¿Country": "Country"})
Emission_2020 = Info_2020[["ï»¿Country", "CO2 emission (Tons)"]].rename(columns ={"CO2 emission (Tons)": "Emissions 2020 (Ton)", "ï»¿Country": "Country"})
#Joining the information  of CO2 emission for each country for to year 1990 and 2020
Emission_1990_2020 = pd.merge(Emission_1990, Emission_2020, on= "Country", how="inner")
#Converting the information to work with numpy
Emission_1990_np = Emission_1990_2020["Emissions 1990 (Ton)"].to_numpy()
Emission_2020_np = Emission_1990_2020["Emissions 2020 (Ton)"].to_numpy()
#Applying the change formula, to know what countries reduced its emissions for 2020
Change_np = ((Emission_2020_np - Emission_1990_np)/Emission_1990_np) * 100
#Creanting a new colmn for to DataFrame Emission_1990_2020 with the information found in variable Change_np
Emission_1990_2020 ["CO2 Reduction (%)"] = Change_np
#Selecting the less emissions, meaning the countries reduced its emissions for the year 2020 and to organize data
Reduce = Emission_1990_2020[Emission_1990_2020["CO2 Reduction (%)"] < 0].sort_values("CO2 Reduction (%)")
#To organice the data to variable CO2 Reduction (%)
Emission_1990_2020.sort_values(by= ["CO2 Reduction (%)"], ascending=True)
#Selecting the 10 firts countries
print(Reduce.head(10))
print("____________________________________________________________________________________")
#Creating the comparison graph
mat.figure(figsize = (12, 6))
x = np.arange(len(Reduce["Country"]))
width = 0.35
mat.bar(x - width/2, Reduce["Emissions 1990 (Ton)"], width, label= "1990", color= "green")
mat.bar(x + width/2, Reduce["Emissions 2020 (Ton)"], width, label= "2020", color= "red")
mat.xticks(x, Reduce["Country"], rotation= 45, ha= "right")
mat.xlabel("Country")
mat.ylabel("CO2 Emissions (Ton)")
mat.title("Comparison of CO₂ Emissions between 1990 and 2020 (Top 10 Reduction")
mat.legend()
mat.tight_layout()
mat.show()


