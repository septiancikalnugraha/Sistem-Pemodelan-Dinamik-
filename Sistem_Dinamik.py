import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Parameter
P_input = 33.0  # daya charger dalam Watt
efficiency = 0.9  # efisiensi pengisian
battery_capacity = 18.5  # kapasitas baterai dalam Wh (misalnya 5000 mAh pada 3.7V)
time_to_full_charge = 3900  # waktu pengisian penuh dalam detik (65 menit)

# Konstanta model
k = 1e-4  # konstanta perlambatan pengisian

# Model pengisian daya
def charging(Q, t, P_input, efficiency, k):
    dQ_dt = P_input * efficiency - k * Q
    return dQ_dt

# Kondisi awal (0% pengisian)
Q0 = 0

# Rentang waktu simulasi
t = np.linspace(0, time_to_full_charge, 400)  # 0 hingga 3900 detik

# Simulasi pengisian
Q = odeint(charging, Q0, t, args=(P_input, efficiency, k))

# Konversi dari Wh ke persentase kapasitas baterai
battery_percentage = (Q / battery_capacity) * 100

# Plot hasil
plt.figure(figsize=(10, 5))
plt.plot(t / 60, battery_percentage, 'b-', label='Persentase Baterai')
plt.xlabel('Waktu (menit)')
plt.ylabel('Level Baterai (%)')
plt.title('Model Pengisian Baterai Handphone dengan Charger 33W')
plt.grid(True)
plt.legend()
plt.show()
