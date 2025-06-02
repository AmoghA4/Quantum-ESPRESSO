import matplotlib.pyplot as plt
import numpy as np
from matplotlib.gridspec import GridSpec
import matplotlib as mpl

# Use a clean serif font suitable for journals
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
energy, Mo = data_loader('PATH TO Molybdenum_Contribution.dat')
_, Se = data_loader('PATH TO/Selenium_Contribution.dat')
_, s = data_loader('PATH TO/sOrbital_Contribution.dat')
_, p = data_loader('PATH TO/pOrbital_Contribution.dat')
_, d = data_loader('PATH TO/dOrbital_Contribution.dat')

# Shift energies by Fermi level
energy_shifted = energy - fermi

# Calculate and plot total projected contribution
tt = Mo + Se 

# Load band structure data
data = np.loadtxt('/PATH TO/unitcell.bands.dat.gnu')
k_values = data[:, 0]
energies = data[:, 1]

# Find band start indices
band_start_indices = [0]
for i in range(1, len(k_values)):
    if k_values[i] < k_values[i - 1]:
        band_start_indices.append(i)
band_start_indices.append(len(k_values))

# Create figure
fig = plt.figure(figsize=(12, 6), dpi=400)
gs = GridSpec(1, 2, width_ratios=[2.5, 1], wspace=0.04)

# --- Band structure plot ---
ax1 = fig.add_subplot(gs[0])
for i in range(len(band_start_indices) - 1):
    start = band_start_indices[i]
    end = band_start_indices[i + 1]
    ax1.plot(k_values[start:end], energies[start:end] - fermi, color='black', linewidth=1.2)

# High symmetry lines and labels
high_symmetry_positions = [0.0, 0.5774, 0.9107, 1.5774]
high_symmetry_labels = ['Γ', 'M', 'K', 'Γ']
for x in high_symmetry_positions:
    ax1.axvline(x=x, color='gray', linestyle='--', linewidth=0.6)
ax1.axhline(y=0, color='gray', linestyle=':', linewidth=1)

ax1.set_xticks(high_symmetry_positions)
ax1.set_xticklabels(high_symmetry_labels)
ax1.set_yticks(np.arange(-7, 8, 1))
ax1.set_xlim(0, 1.5774)
ax1.set_ylim(-7, 7)
ax1.set_ylabel('Energy (eV)', labelpad=10)
ax1.set_xlabel('High Symmetry Points', labelpad=8)
ax1.grid(True, linestyle='-.', linewidth=0.4, alpha=0.5)

# --- DOS plot ---
ax2 = fig.add_subplot(gs[1], sharey=ax1)
ax2.plot(0.4*tt, energy_shifted, color='black', linewidth=1.2)
ax2.axhline(y=0, color='gray', linestyle=':', linewidth=1, label='Fermi')

# Fill bands
ax2.fill_between(0.4*tt, energy_shifted, where=energy_shifted < 0,
                 facecolor='blue', alpha=0.3, hatch='///', edgecolor='black',
                 linewidth=0.0, label='VB')

ax2.fill_between(0.4*tt, energy_shifted, where=energy_shifted > 0,
                 facecolor='red', alpha=0.3, hatch='\\\\\\', edgecolor='black',
                 linewidth=0.0, label='CB')

ax2.set_xlim(0, 1)
ax2.set_xticks(np.arange(0.2, 1.1, 0.2))
ax2.set_xlabel("Normalised DOS", labelpad=8)
ax2.set_ylabel("Energy (eV)", rotation=270, labelpad=15)
ax2.yaxis.set_ticks_position('right')
ax2.yaxis.set_label_position("right")
plt.setp(ax2.get_yticklabels(), visible=False)
ax2.grid(True, linestyle='--', linewidth=0.4, alpha=0.5)

# Legend outside for cleaner look
ax2.legend(loc='upper left', bbox_to_anchor=(0.55, 1), borderaxespad=0.0, frameon=False)

# Title (optional or replace with figure caption in journal)
#fig.suptitle("Electronic Band Structure and DOS of Pristine MoSe₂ Unitcell", fontsize=16, y=0.97)

# Save high-quality figure
plt.savefig('WHERE DO YOU WANNA SAVE/Bands+DOS (PU).jpg',
            dpi=400, bbox_inches='tight', transparent=True)
plt.close()

