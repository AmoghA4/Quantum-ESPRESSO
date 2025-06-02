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
    'legend.fontsize': 16,
    'axes.linewidth': 1,
    'xtick.direction': 'in',
    'ytick.direction': 'in',
    'xtick.major.size': 5,
    'ytick.major.size': 5,
})

# Load band structure data
data = np.loadtxt('   PATH TO    unitcell.bands.dat.gnu')
k_values = data[:, 0]
energies = data[:, 1]

# Fermi energy and shift
fermi_energy = -4.2181 # eV
energies_shifted = energies - fermi_energy

# Detect band start indices
band_start_indices = [0]
for i in range(1, len(k_values)):
    if k_values[i] < k_values[i - 1]:
        band_start_indices.append(i)
band_start_indices.append(len(k_values))

# Create figure
fig, ax = plt.subplots(figsize=(12, 6), dpi=400)

# Plot each band segment
for i in range(len(band_start_indices) - 1):
    start = band_start_indices[i]
    end = band_start_indices[i + 1]
    ax.plot(k_values[start:end], energies_shifted[start:end], linewidth=1.2, color='black')

# High symmetry points and labels
high_symmetry_positions = [0.0, 0.5774, 0.9107, 1.5774]
high_symmetry_labels = ['Γ', 'M', 'K', 'Γ']
for x in high_symmetry_positions:
    ax.axvline(x=x, color='gray', linestyle='--', linewidth=0.6)

# Fermi energy line
ax.axhline(y=0, linestyle=':', linewidth=1, color='gray', label='Fermi Level')

# Axis settings
ax.set_xlim(0, 1.5774)
ax.set_ylim(-7, 7)
ax.set_yticks(np.arange(-7, 8, 1))
ax.set_xticks(high_symmetry_positions)
ax.set_xticklabels(high_symmetry_labels)
ax.set_xlabel("High Symmetry Points", labelpad=8)
ax.set_ylabel("Energy (eV)", labelpad=10)
ax.grid(True, linestyle='-.', linewidth=0.4, alpha=0.5)

# Legend
ax.legend(loc="upper right", frameon=False)

# Title
fig.suptitle("Electronic Band Structure of Pristine MoSe₂ Unitcell", fontsize=16, y=0.97)

# Save figure
plt.savefig('/WHERE DO YOU WANNA SAVE',
            dpi=400, bbox_inches='tight', transparent=True)
plt.close()

