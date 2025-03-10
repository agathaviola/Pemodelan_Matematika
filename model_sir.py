# -*- coding: utf-8 -*-
"""Model SIR

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1S8BPQ0P6FeuHKI28LnJHYw2WUlfwSYbA
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Parameter model
beta = 0.2            #Laju infeksi
gamma = 1/10          #Laju pemulihan (1/gamma = 10 hari)
N = 1000              #Total populasi

# Kondisi awal
S0 = N - 1             #Semua adalah individu rentan kecuali 1 yang terinfeksi
I0 = 1                 #Individu terinfeksi pada awalnya
R0 = 0                 #Tidak ada yang sembuh pada awalnya

# Waktu Simulasi (dalam hari)
t = np.linspace(0, 160, 160) # Simulasi selama 160 hari

# Model SIR
def sir_model(y, t, N, beta, gamma):
  S, I, R = y
  dSdt = -beta * S * I / N
  dIdt = beta * S * I / N - gamma * I
  dRdt = gamma * I
  return [dSdt, dIdt, dRdt]
# Menyelesaikan sistem persamaan diferensial
y0 = [S0, I0, R0]
solution = odeint(sir_model, y0, t, args=(N, beta, gamma))
S, I, R = solution.T

# Plot hasil simulasi
plt.figure(figsize=(10,6))
plt.plot(t, S, label='Susceptible', color='blue')
plt.plot(t, I, label="Infected", color='red')
plt.plot(t, R, label='Recovered', color='green')
plt.xlabel('Hari')
plt.ylabel('Jumlah individu')
plt.title('Simulasi Model SIR')
plt.legend()
plt.grid()
plt.show()

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import ipywidgets as widgets
from IPython.display import display

#Model SIR
def sir_model(y, t, N, beta, gamma):
  S, I, R = y
  dSdt = -beta * S * I / N
  dIdt = beta * S * I / N - gamma * I
  dRdt = gamma * I
  return [dSdt, dIdt, dRdt]
# Fungsi untuk memperbarui grafik
def update_sir(beta, gamma, S0, I0, Tmax):
  N = S0 + I0 #Total populasi
  R0 = 0 #Tidak ada yang sembuh pada awalnya
  t = np.linspace(0, Tmax, Tmax) #Waktu simulasi

  #Menyelesaikan sistem persamaan diferensial
  y0 = [S0, I0, R0]
  solution = odeint(sir_model, y0, t, args=(N, beta, gamma))
  S, I, R = solution.T
  plt.figure(figsize=(10,6))
  plt.plot(t, S, label='Susceptible', color='blue')
  plt.plot(t, I, label="Infected", color='orange')
  plt.plot(t, R, label='Recovered', color='green')
  plt.xlabel('Hari')
  plt.ylabel('Jumlah individu')
  plt.title('Simulasi Model SIR')
  plt.legend()
  plt.grid()
  plt.show()

#Membuat slider interaktif
widgets.interactive(update_sir,
                    beta=widgets.FloatSlider(min=0.0001, max=1, step=0.0001, value=0.2, description='b'),
                    gamma=widgets.FloatSlider(min=0.01, max=1, step=0.01, value=0.1, description='y'),
                    S0=widgets.IntSlider(min=1, max=1000, step=1, value=997, description='So'),
                    I0=widgets.IntSlider(min=1, max=100, step=1, value=3, description='Io'),
                    Tmax=widgets.IntSlider(min=10, max=200, step=10, value=100, description='Tmax'))