#nilai ujian teori dan praktek minimal 70
nilai_t = 70
nilai_p = 70
print("jika nilai ujian teori dan praktek minimal", str(nilai_t))

if nilai_t >=70 and nilai_p >= 70:
  print("Selamat, anda lulus!.")
elif nilai_t >=70 and nilai_p <= 70:
  print("Anda harus mengulang ujian praktek.")
elif nilai_t <=70 and nilai_p >= 70:
  print("Anda harus mengulang ujian teori.")
elif nilai_t <=70 and nilai_p <= 70:
  print("Anda harus mengulang ujian teori dan praktek.")

#nilai ujian teori minimal 70 dan ujian praktek kurang dari 70
nilai_t = 70
nilai_p = 60
print("Jika nilai ujian teori minimal", str(nilai_t), "dan nilai ujian praktek kurang dari", str(nilai_t))

if nilai_t >=70 and nilai_p >= 70:
  print("Selamat, anda lulus!.")
elif nilai_t >=70 and nilai_p <= 70:
  print("Anda harus mengulang ujian praktek.")
elif nilai_t <=70 and nilai_p >= 70:
  print("Anda harus mengulang ujian teori.")
elif nilai_t <=70 and nilai_p <= 70:
  print("Anda harus mengulang ujian teori dan praktek.")


#nilai ujian teori kurang dari 70 dan ujian praktek minimal 70
nilai_t = 60
nilai_p = 70
print("Jika nilai ujian teori kurang dari", str(nilai_p), "dan nilai ujian praktek minimal", str(nilai_p))

if nilai_t >=70 and nilai_p >= 70:
  print("Selamat, anda lulus!.")
elif nilai_t >=70 and nilai_p <= 70:
  print("Anda harus mengulang ujian praktek.")
elif nilai_t <=70 and nilai_p >= 70:
  print("Anda harus mengulang ujian teori.")
elif nilai_t <=70 and nilai_p <= 70:
  print("Anda harus mengulang ujian teori dan praktek.")

#nilai ujian teori dan ujian praktek kurang dari 70
nilai_t = 60
nilai_p = 60
print("Jika nilai ujian teori dan praktek adalah", str(nilai_p))

if nilai_t >=70 and nilai_p >= 70:
  print("Selamat, anda lulus!.")
elif nilai_t >=70 and nilai_p <= 70:
  print("Anda harus mengulang ujian praktek.")
elif nilai_t <=70 and nilai_p >= 70:
  print("Anda harus mengulang ujian teori.")
elif nilai_t <=70 and nilai_p <= 70:
  print("Anda harus mengulang ujian teori dan praktek.")
