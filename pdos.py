import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
from matplotlib.gridspec import GridSpec

# Set global plot styling (serif font, clear, professional)
mpl.rcParams.update({
    'font.family': 'serif',
    'font.size': 12,
    'axes.labelsize': 14,
    'xtick.labelsize': 12,
    'ytick.labelsize': 12,
    'legend.fontsize': 12,
    'axes.linewidth': 1,
    'legend.fontsize': 14,
    'xtick.direction': 'in',
    'ytick.direction': 'in',
    'xtick.major.size': 5,
    'ytick.major.size': 5,
})

# Define Fermi energy (eV)
fermi = -4.2181

# Data loader function for consistency
def data_loader(fname):
    data = np.loadtxt(fname)
    energy = data[:, 0]
    pdos = data[:, 1]
    return energy, pdos

# Load data
energy, Mo = data_loader('/home/amogh-a/Study Project/Unitcell/Pristine/Plots/Molybdenum_Contribution.dat')
_, Se = data_loader('/home/amogh-a/Study Project/Unitcell/Pristine/Plots/Selenium_Contribution.dat')
_, s = data_loader('/home/amogh-a/Study Project/Unitcell/Pristine/Plots/sOrbital_Contribution.dat')
_, p = data_loader('/home/amogh-a/Study Project/Unitcell/Pristine/Plots/pOrbital_Contribution.dat')
_, d = data_loader('/home/amogh-a/Study Project/Unitcell/Pristine/Plots/dOrbital_Contribution.dat')

# Shift energies by Fermi level
energy_shifted = energy - fermi

# Create figure
fig, ax = plt.subplots(figsize=(12, 6), dpi=400)

# Calculate and plot total projected contribution
tt = Mo + Se 
ax.plot(energy_shifted, 0.4*tt, color='blue', linewidth=1.2, label='Total DOS')

# Plot each PDOS contribution
ax.plot(energy_shifted, 0.4*Mo, color='black', linewidth=1.2, label='Molybdenum')
ax.plot(energy_shifted, 0.4*Se, color='saddlebrown', linewidth=1.2, label='Selenium')
ax.plot(energy_shifted, 0.4*s, color='green', linewidth=1.2, label='s Orbital')
ax.plot(energy_shifted, 0.4*p, color='crimson', linewidth=1.2, label='p Orbital')
ax.plot(energy_shifted, 0.4*d, color='goldenrod', linewidth=1.2, label='d Orbital')

# Fermi level line
ax.axvline(x=0, color='gray', linestyle=':', linewidth=1.2, label='Fermi Level')

# Axis limits and ticks
ax.set_xlim(-7, 7)
ax.set_ylim(0,1)
ax.set_xticks(np.arange(-7, 8, 1))
ax.set_yticks(np.arange(0, 1.1, 0.1))

# Labels and title
ax.set_xlabel("Energy (eV)", labelpad=8)
ax.set_ylabel("Normalised DOS", labelpad=10)
#fig.suptitle("Projected Density of States of Pristine MoSe₂ Unitcell", fontsize=16, y=0.97)

# Grid and legend
ax.grid(True, linestyle='--', linewidth=0.4, alpha=0.4)
ax.legend(loc='upper right', frameon=False)

# Save figure
plt.savefig('/home/amogh-a/Study Project/Unitcell/Pristine/Plots/Projected Density of States (PU).jpg',
            dpi=400, bbox_inches='tight', transparent=True)
plt.close()

