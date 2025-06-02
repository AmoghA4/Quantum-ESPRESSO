# Import required libraries
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

# Set global plot parameters for journal-quality consistency
mpl.rcParams.update({
    'font.family': 'serif',
    'font.size': 12,
    'axes.labelsize': 14,
    'xtick.labelsize': 12,
    'ytick.labelsize': 12,
    'legend.fontsize': 12,
    'axes.linewidth': 1,
    'legend.fontsize': 16,
    'xtick.direction': 'in',
    'ytick.direction': 'in',
    'xtick.major.size': 5,
    'ytick.major.size': 5,
})

# Data loader function for consistency
def data_loader(fname):
    data = np.loadtxt(fname)
    energy = data[:, 0]
    pdos = data[:, 1]
    return energy, pdos

# Define Fermi level (in eV)
fermi = -4.2181

# Load data
energy, Mo = data_loader('PATH TO/Molybdenum_Contribution.dat')
_, Se = data_loader('PATH TO/Selenium_Contribution.dat')
_, s = data_loader('PATH TO/Plots/sOrbital_Contribution.dat')
_, p = data_loader('PATH TO/pOrbital_Contribution.dat')
_, d = data_loader('PAHT TO/dOrbital_Contribution.dat')

# Shift energies by Fermi level
energy_shifted = energy - fermi

# Create figure
fig, ax = plt.subplots(figsize=(12, 6), dpi=400)

# Calculate and plot total projected contribution
tt = Mo + Se 
ax.plot(energy_shifted, 0.4*tt, color='black', linewidth=1.2, label='DOS')

# Fermi energy line
ax.axvline(x=0, color='gray', linestyle=':', linewidth=1, label='Fermi Level')

# Fill valence and conduction bands
ax.fill_between(energy_shifted, tt*0.4, where=energy_shifted < 0,
                facecolor='blue', alpha=0.3, hatch='///', edgecolor='black', linewidth=0.0,
                label='Valence Band')

ax.fill_between(energy_shifted, tt*0.4, where=energy_shifted > 0,
                facecolor='red', alpha=0.3, hatch='\\\\\\', edgecolor='black', linewidth=0.0,
                label='Conduction Band')

# Axis limits and ticks
ax.set_xlim(-7, 7)
ax.set_ylim(0, 1)
ax.set_xticks(np.arange(-7, 8, 1))
ax.set_yticks(np.arange(0, 1.1, 0.1))

# Labels and styling
ax.set_xlabel("Energy (eV)", labelpad=8)
ax.set_ylabel("Normalised DOS", labelpad=10)
ax.grid(True, linestyle='--', linewidth=0.4, alpha=0.5)
ax.legend(loc="upper right", frameon=False)

# Title
#fig.suptitle("Density of States of Pristine MoSe₂ Unitcell", fontsize=16, y=0.97)

# Save high-quality plot
plt.savefig('WHERE DO YOU WANNA SAVE/Density of States (PU).jpg',
            dpi=400, bbox_inches='tight', transparent=True)
plt.close()

