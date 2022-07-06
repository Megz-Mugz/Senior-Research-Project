import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
plt.style.use("dark_background")
# sns.set_theme(style="")

df = pd.read_csv("microplasticBioaccumulation.csv")

first_day = []
second_day = []
third_day = []
for i in df.index:
    if df["Date"][i] == "2022-01-26":
        first_day.append(df["MP-Particles"][i])
    if df["Date"][i] == "2022-02-02":
        second_day.append(df["MP-Particles"][i])
    if df["Date"][i] == "2022-02-10":
        third_day.append(df["MP-Particles"][i])

#
#
lm = sns.lmplot(x= "Day-Number", y="MP-Particles", data=df, x_estimator=np.mean).set(
    title="Microplastic Bioaccumulation Over Time", ylabel="Microplastic Particles",
xlabel="Day Number")
print(third_day)
# plt.savefig("lm.png")
# print("there will be an output in the console... like so")
# print("there will be an output in the console... like so")
# print("there will be an output in the console... like so")

plt.show()

