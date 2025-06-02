import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
import re

# Set global plot styling
mpl.rcParams.update({
    'font.family': 'serif',
    'font.size': 12,
    'axes.labelsize': 14,
    'xtick.labelsize': 12,
    'ytick.labelsize': 12,
    'legend.fontsize': 16,
    'axes.linewidth': 1,
    'xtick.direction': 'in',
    'ytick.direction': 'in',
    'xtick.major.size': 5,
    'ytick.major.size': 5,
})

# Load and clean phonon dispersion data
filepath = "/home/amogh-a/Study Project/Unitcell/Pristine/Plots/matdyn.freq.gp"
clean_data = []

with open(filepath, 'r') as f:
    for line in f:
        # Insert space between numbers if missing (e.g. -2364.9300-2364.9300 → -2364.9300 -2364.9300)
        cleaned_line = re.sub(r'(?<=\d)-', ' -', line.strip())
        parts = cleaned_line.split()
        try:
            clean_data.append([float(x) for x in parts])
        except ValueError:
            print(f"Skipping line due to error: {line.strip()}")

data = np.array(clean_data)
nbands = data.shape[1] - 1
k_values = data[:, 0]

# Create figure
fig, ax = plt.subplots(figsize=(12, 6), dpi=400)

# Plot each phonon branch
for band in range(1, nbands + 1):
    ax.plot(k_values, data[:, band], linewidth=1.2, color='black')

# High symmetry points and labels
#high_sym_indices = [0, 20, 40, 60]
#high_sym_labels = [r'$\Gamma$', 'M', 'K', r'$\Gamma$']
#xtick_positions = [k_values[i] for i in high_sym_indices]
#for x in xtick_positions:
#    ax.axvline(x=x, color='gray', linestyle='--', linewidth=0.6)

# Axis settings
#ax.set_xticks(xtick_positions)
#ax.set_xticklabels(high_sym_labels)
ax.set_xlim(0, 117.010498)
ax.set_ylim(0, 3200)
#ax.set_xlabel("High Symmetry Points", labelpad=8)
ax.set_ylabel("Frequency (cm$^{-1}$)", labelpad=10)
ax.grid(True, linestyle='-.', linewidth=0.4, alpha=0.5)

# Title
fig.suptitle("Phonon Dispersion in Pristine MoSe₂ Unitcell", fontsize=16, y=0.97)

# Save figure
plt.savefig("/home/amogh-a/Study Project/Unitcell/Pristine/Plots/Phonon Dispersion (PU).jpg",
            dpi=400, bbox_inches='tight', transparent=True)
plt.close()

