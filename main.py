import pandas as pd
import matplotlib.pyplot as plt

# Read COVID data
df = pd.read_csv("./data/covid_data_bulgaria.csv")
df.set_index(["Дата"])[["Хоспитализирани", "Починали"]].\
    plot(figsize=(13, 13))

# Read COVID deaths by age and gender data
deaths_df = pd.read_csv("./data/covid_deaths_by_age_and_gender.csv")
mapped_df = deaths_df[deaths_df["Възрастова група"] != '-']
gdf = mapped_df.groupby("Възрастова група").sum(numeric_only=True)
gdf.columns = [""]
outer_color = ["#FF98D2", "#FFB67A", "#FFDE2B", "#FFFF00",
               "#93FF60", "#00FFBC", "#00FFFF", "#00D1D1",
               "#00A3A3", "#007575", "#275D5D", "#193D3C"]

gdf.plot.pie(title="Смъртност от Covid-19 по възрастови групи в България",
             subplots=True, labeldistance=None, figsize=(18, 16), fontsize=50,
             colors=outer_color)


df.set_index(["Дата"])[["Тестове за денонощие", "Излекувани за денонощие",
                        "Починали за денонощие", "Нови случаи за денонощие"]].\
                            plot(figsize=(13, 13))
regions = pd.read_csv("./data/covid_data_by_regions.csv")
usable_regions = regions[["Дата", "BLG_ACT", "BGS_ACT", "VAR_ACT", "VTR_ACT",
                          "RSE_ACT", "SML_ACT", "JAM_ACT"]]
usable_regions.columns = ["Дата", "Благоевград", "Бургас", "Варна",
                          "Велико Търново", "Русе", "Смолян", "Ямбол"]
usable_regions.set_index(["Дата"]).plot(figsize=(20, 15))
plt.show()
