hop_sach = ['van', 'su', 'dia']

print(hop_sach[0])
print(hop_sach[1])
print(hop_sach[2])

hop_sach[0] = 'van hoc'
hop_sach[1] = 'lich su'
hop_sach[2] = 'dia ly'
hop_sach.append('toan')
hop_sach.append('ly')
hop_sach.append('hoa')
hop_sach.sort(reverse=True)

print(hop_sach)