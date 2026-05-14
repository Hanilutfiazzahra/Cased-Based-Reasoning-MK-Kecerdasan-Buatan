import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import matplotlib.pyplot as plt
import numpy as np

# ── Fungsi keanggotaan harga ───────────────────────────────────────────
def harga_ekonomis(x):
    if x <= 25000:  return 1
    elif x < 30000: return (30000 - x) / 5000
    else:           return 0

def harga_standar(x):
    if x <= 25000:   return 0
    elif x < 40000:  return (x - 25000) / 15000
    elif x < 55000:  return (55000 - x) / 15000
    else:            return 0

def harga_premium(x):
    if x <= 40000:  return 0
    elif x < 55000: return (x - 40000) / 15000
    else:           return 1

# ── Grafik Variabel Harga ──────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(10, 5))

x_harga    = np.linspace(25000, 60000, 500)
y_ekonomis = [harga_ekonomis(x) for x in x_harga]
y_standar  = [harga_standar(x)  for x in x_harga]
y_premium  = [harga_premium(x)  for x in x_harga]

ax.plot(x_harga, y_ekonomis, label='Harga Ekonomis', color='blue',   linewidth=2)
ax.plot(x_harga, y_standar,  label='Harga Standar',  color='purple', linewidth=2)
ax.plot(x_harga, y_premium,  label='Harga Premium',  color='brown',  linewidth=2)
ax.set_title('Grafik Fungsi Keanggotaan Variabel Harga', fontsize=13, fontweight='bold')
ax.set_xlabel('Nilai Harga (Rp)')
ax.set_ylabel('Derajat Keanggotaan')
ax.set_xlim(25000, 60000)
ax.set_ylim(0, 1.1)
ax.legend()
ax.grid(True, linestyle='--', alpha=0.5)
ax.set_xticks([25000, 30000, 40000, 55000, 60000])
ax.tick_params(axis='x', rotation=30)

plt.tight_layout()
plt.savefig('grafik_harga.png', dpi=150, bbox_inches='tight')
plt.show()
print("Grafik harga disimpan sebagai grafik_harga.png")