#positif
phi = float(22/7)
r = int(14)
luas = float(22/7*14*14)
c = ("\u00b2")

rumus = "luas lingkarang dengan jari-jari {} cm adalah {} cm{}".format (r, luas, c)
print(rumus)

#desimal
phi = float(22/7)
r = float(10)
luas = float(22/7*10*10)
c = ("\u00b2")

rumus = "luas lingkarang dengan jari-jari {} cm adalah {} cm{}".format (r, luas, c)
print(rumus)

#dibulatkan
phi = float(22/7)
r = int(10)
luas = float(22/7*10*10)
c = ("\u00b2")

kalimat = "luas lingkarang dengan jari-jari {} cm adalah {:.2f} cm".format (r, 314.2857142857143)
print(kalimat+c)