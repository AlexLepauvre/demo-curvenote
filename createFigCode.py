# Import required libraries
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.formula.api as smf
import scipy.stats as stats
import pylustrator

# Step 1: Load the Palmer Penguins dataset
# Seaborn provides a direct function to load the dataset
penguins = sns.load_dataset('penguins')


penguins_clean = penguins.dropna()
# Compute the regression between the body mass, bill length and species:
model = smf.ols('body_mass_g ~ bill_length_mm * species', data=penguins).fit()
residuals = model.resid
fitted_values = model.fittedvalues
x_range = np.linspace(penguins['bill_length_mm'].min(), penguins['bill_length_mm'].max(), 100)
# Plot the results:
pylustrator.start()
fig, axs = plt.subplots(1, 3, figsize=(15, 5), sharey=False)

# Plot 1: Correlation between bill length and body mass with individual points and average trend
colors = {'Adelie': 'blue', 'Chinstrap': 'green', 'Gentoo': 'orange'}
for species, group in penguins.groupby('species'):
    axs[0].scatter(group['bill_length_mm'], group['body_mass_g'], label=f'{species}', color=colors[species], alpha=0.7)
    species_model = smf.ols('body_mass_g ~ bill_length_mm', data=group).fit()
    axs[0].plot(
        x_range,
        species_model.params[0] + species_model.params[1] * x_range,
        color=colors[species],
        label=f'{species} Trend'
    )
axs[0].set_title('Correlation Between Bill Length and Body Mass')
axs[0].set_xlabel('Bill Length (mm)')
axs[0].set_ylabel('Body Mass (g)')
axs[0].legend()

# Plot 2: QQ Plot of residuals
stats.probplot(residuals, dist="norm", plot=axs[1])
axs[1].get_lines()[1].set_color('red')  # Make the trend line red
axs[1].set_title('QQ Plot of Residuals')

# Plot 3: Residuals vs. Fitted Values (Assumption check for homoscedasticity)
axs[2].scatter(fitted_values, residuals, alpha=0.7, color='purple')
axs[2].axhline(0, color='red', linestyle='--')
axs[2].set_title('Residuals vs. Fitted Values')
axs[2].set_xlabel('Fitted Values')
axs[2].set_ylabel('Residuals')

# Adjust layout and display the plots
plt.tight_layout()
plt.show()

