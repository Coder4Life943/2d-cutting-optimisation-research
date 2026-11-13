
from rectpack import newPacker

# 1. Create the optimiser
packer = newPacker(rotation=True)

# 2. Add steel plate
packer.add_bin(5000, 4000)

# 3. Add requested parts
packer.add_rect(3000, 2000, rid="A")
packer.add_rect(1500, 1000, rid="B")
packer.add_rect(6000, 1000, rid="C")

requested_parts = ["A", "B", "C"]

# 4. Run optimisation
packer.pack()

# 5. Read successfully packed components
packed_parts = []
used_area = 0

for bin_index, x, y, width, height, rect_id in packer.rect_list():
    packed_parts.append(rect_id)
    used_area = used_area + (width * height)

# 6. Identify unpacked components
unpacked_parts = []

for part in requested_parts:
    if part not in packed_parts:
        unpacked_parts.append(part)

# 7. Calculate material utilisation
plate_area = 5000 * 4000

utilisation = (used_area / plate_area) * 100
unused_percentage = 100 - utilisation

# 8. Report results
print("GOSMARTER OPTIMISATION REPORT")
print("----------------------------")
print("Packed parts:", packed_parts)
print("Unpacked parts:", unpacked_parts)
print("Used area:", used_area, "mm²")
print("Utilisation:", utilisation, "%")
print("Unused material:", unused_percentage, "%")
print("Parts requested:", len(requested_parts))
print("Parts packed:", len(packed_parts))
print("Order complete:", len(unpacked_parts) == 0)
