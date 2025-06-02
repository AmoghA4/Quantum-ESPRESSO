# Import required libraries
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

# Set global plot styling
mpl.rcParams.update({
    'font.family': 'serif',
    'font.size': 12,
    'axes.labelsize': 14,
    'xtick.labelsize': 12,
    'ytick.labelsize': 12,
    'legend.fontsize': 12,
    'axes.linewidth': 1,
    'xtick.direction': 'in',
    'ytick.direction': 'in',
    'legend.fontsize': 16,
    'xtick.major.size': 5,
    'ytick.major.size': 5,
})

# Load phonon DOS data
freq, dos, pdos_Mo, pdos_Se, hi = np.loadtxt("/home/amogh-a/Study Project/Unitcell/Pristine/Plots/MoSe2.phdos", unpack=True)

# Create figure
fig, ax = plt.subplots(figsize=(12, 6), dpi=400)

# Plot the data
ax.plot(freq, dos, color='black', linewidth=1.2, label='Total')
ax.plot(freq, pdos_Mo, color='blue', linewidth=1.2, label='Mo')
ax.plot(freq, pdos_Se, color='red', linewidth=1.2, label='Se')

# Axis limits and ticks
ax.set_xlim(-6000, 6000)
ax.set_ylim(0, 0.07)
ax.set_xticks(np.arange(-6000, 6001, 100))
ax.set_yticks(np.arange(0, 10000, 1000))

ax.set_xlabel(r'$\Omega~(\mathrm{cm}^{-1})$', labelpad=8)
ax.set_ylabel(r'Phonon DOS (states/cm$^{-1}$)', labelpad=10)
ax.grid(True, linestyle='-.', linewidth=0.4, alpha=0.5)

# Legend
ax.legend(loc='upper right', frameon=False)

# Title
#fig.suptitle("Phonon Density of States in Pristine MoSe₂ Unitcell", fontsize=16, y=0.97)

# Save figure
plt.savefig("/home/amogh-a/Study Project/Unitcell/Pristine/Plots/Phonon DOS (PU).jpg",
            dpi=400, bbox_inches='tight', transparent=True)
plt.close()

