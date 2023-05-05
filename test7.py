metal_on_instrument=7
metal_on_gvoshd=0.6
all_metal=40
number_of_instruments=all_metal//metal_on_instrument
print(number_of_instruments)
#
#ne_ostatok=metal_on_instrument*number_of_instruments
#ostatok=all_metal-ne_ostatok

ostatok=all_metal%metal_on_instrument
number_of_gvoshd=ostatok//metal_on_gvoshd
print(number_of_gvoshd)
ostalos=ostatok%metal_on_gvoshd
#ostalos=all_metal-ne_ostatok-metal_on_gvoshd*number_of_gvoshd
print(ostalos)



