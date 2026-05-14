import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import matplotlib.pyplot as plt
import numpy as np

# ── Fungsi keanggotaan servis ──────────────────────────────────────────
def servis_rendah(x):
    if x <= 40:   return 1
    elif x < 60:  return (60 - x) / 20
    else:         return 0

def servis_cukup(x):
    if x <= 40:   return 0
    elif x < 60:  return (x - 40) / 20
    elif x < 80:  return (80 - x) / 20
    else:         return 0

def servis_memuaskan(x):
    if x <= 60:   return 0
    elif x < 80:  return (x - 60) / 20
    else:         return 1

# ── Grafik Variabel Servis ─────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(10, 5))

x_servis    = np.linspace(0, 100, 500)
y_rendah    = [servis_rendah(x)    for x in x_servis]
y_cukup     = [servis_cukup(x)     for x in x_servis]
y_memuaskan = [servis_memuaskan(x) for x in x_servis]

ax.plot(x_servis, y_rendah,    label='Servis Rendah',    color='red',    linewidth=2)
ax.plot(x_servis, y_cukup,     label='Servis Cukup',     color='orange', linewidth=2)
ax.plot(x_servis, y_memuaskan, label='Servis Memuaskan', color='green',  linewidth=2)
ax.set_title('Grafik Fungsi Keanggotaan Variabel Servis', fontsize=13, fontweight='bold')
ax.set_xlabel('Nilai Servis')
ax.set_ylabel('Derajat Keanggotaan')
ax.set_xlim(0, 100)
ax.set_ylim(0, 1.1)
ax.legend()
ax.grid(True, linestyle='--', alpha=0.5)
ax.set_xticks([0, 20, 40, 60, 80, 100])

plt.tight_layout()
plt.savefig('grafik_servis.png', dpi=150, bbox_inches='tight')
plt.show()
print("Grafik servis disimpan sebagai grafik_servis.png")