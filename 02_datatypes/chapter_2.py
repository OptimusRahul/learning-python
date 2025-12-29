spice_mix = set ()
print(f"Initial spice mix: {id(spice_mix)}")
print(f"Initial spice mix: {spice_mix}")

spice_mix.add("cumin")
print(f"Spice mix after adding cumin: {id(spice_mix)}")
print(f"Spice mix after adding cumin: {spice_mix}")
        
spice_mix.add("coriander")
print(f"Spice mix after adding coriander: {id(spice_mix)}")
print(f"Spice mix after adding coriander: {spice_mix}")

spice_mix.add("cumin")
print(f"Spice mix after adding cumin again: {id(spice_mix)}")
print(f"Spice mix after adding cumin again: {spice_mix}")