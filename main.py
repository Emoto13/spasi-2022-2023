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
outer_color = ["#808000", "#BA4A00", "#808080", "#229954", "#34495E",
               "#2E86C1", "#CA6F1E", "#16A085", "#808080", "#229954",
               "#F2D2BD", "#00FFFF"]
gdf.plot.pie(title="Смъртност от Covid-19 по възрастови групи в България",
             subplots=True, labeldistance=None, figsize=(18, 16), fontsize=50,
             colors=outer_color)


df.set_index(["Дата"])[["Тестове за денонощие", "Излекувани за денонощие",
                        "Починали за денонощие", "Нови случаи за денонощие"]].\
                            plot(figsize=(13, 13))

plt.show()
