import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import ExponentialSmoothing

plt.style.use("dark_background")

# training data
training_data = pd.read_csv("Microplastic Forecast.csv", index_col="Date", parse_dates=True).asfreq("3D")


model = ExponentialSmoothing(training_data["MP Particles"],
            trend="add", damped_trend=True).fit(smoothing_level=0.8, damping_trend=0.9)

print(model.forecast(5))