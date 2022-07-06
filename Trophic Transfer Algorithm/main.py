import pandas as pd
import matplotlib.pyplot as plt
import random
import numpy as np
plt.style.use("dark_background")

# training data for exp. smoothing model
df = pd.read_csv("collected and forecasted data.csv", index_col="Date", parse_dates=True)

edible = 63.784 # grams

# variables for function
plasticConcentration = 0.3 # in mg / g

total_consumedMPs = []
totalMPs = ''
concentrationTotal = edible * plasticConcentration
eachTrialdaphnia = []
eachTrialTotal = []


def microplasticsEaten():
    global consumed_MPs, totalMPs
    consumedMPs = []
    for x in range(0, 111):
        day = random.randrange(0, 11)
        daphniaMP = df["MP Particles"][day]
        consumedMPs.append(daphniaMP)


    consumed_MPs = sum(consumedMPs)
    eachTrialdaphnia.append(consumed_MPs)

    totalMPs = consumed_MPs * 10
    eachTrialTotal.append(totalMPs)


for y in range(0, 10001):
    microplasticsEaten()


print(f'Consumed Microplastics Total: {np.mean(eachTrialTotal).round(2)}')
print(f'Consumed Microplastics From Daphnia: {np.mean(eachTrialdaphnia).round(2)}')

print('--------------------')
print(f'concentration: {(concentrationTotal / 10).__round__(2)} mg MPs from daphnia ')
