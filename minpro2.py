users = {
    "admin": {"password": "adm123", "role": "admin"},
    "member": {"password": "88yao", "role": "member"}
}

target_bulanan = []

def login():
    print("=== Login Sistem Target Bulanan ===")
    for percobaan in range(4):
        username = input("Username: ")
        password = input("Password: ")

        if username in users and users[username]["password"] == password:
            role = users[username]["role"]
            print(f"Login berhasil! Selamat datang {username} ({role})")
            return role
        else:
            sisa = 3 - percobaan
            if sisa > 0:
                print(f"Username atau password salah! Sisa percobaan: {sisa}")
            else:
                print("Sisa login anda habis, silahkan login ulang")

def menu(role):
    while True:
        print("=== Menu Target Bulanan ===")
        if role == "admin":
            print("1. Tambah target")
            print("2. Lihat target")
            print("3. Update progress")
            print("4. Hapus target")
            print("5. Logout")

        elif role == "member":
            print("1. Tambah target")
            print("2. Update progress")
            print("3. Logout")

        pilihan = input("Pilih menu: ")

        if role == "admin":
            if pilihan == "1":
                    nama = input("Masukkan target baru: ")
                    deadline = input("Masukkan deadline target (contoh: 30 September 2025): ")
                    target_bulanan.append ({
                        "nama": nama,
                        "progress": 0,
                        "deadline": deadline
                    })
                    print("Target berhasil ditambahkan!")

            elif pilihan == "2":
                if not target_bulanan:
                    print("Belum ada target")
                else:
                    print("=== Daftar Target Bulanan ===")
                    for i, target in enumerate(target_bulanan, start=1):
                        print(f"{i}. {target['nama']} - {target['progress']}% (Deadline: {target['deadline']})")

            elif pilihan == "3":
                if not target_bulanan:
                    print("Belum ada target untuk diupdate")
                else:
                    try:
                        print("=== Daftar Target ===")
                        for i, target in enumerate(target_bulanan, start=1):
                            print(f"{i}. {target['nama']} - {target['progress']}% (Deadline: {target['deadline']})")

                        pilih = int(input("Pilih nomor yang ingin diupdate: "))
                        if 1 <= pilih <= len(target_bulanan):
                            progress_baru = int(input("Masukkan progress baru (0-100): "))
                        else:
                            print("Nomor target tidak valid!")
                    except ValueError:
                        print("Input harus angka!")

            elif pilihan == "4":
                if not target_bulanan:
                    print("Belum ada target untuk dihapus")
                else:
                    try:
                        print("=== Daftar Target ===")
                        for i, target in enumerate(target_bulanan, start=1):
                            print(f"{i}. {target['nama']} - {target['progress']}% (Deadline: {target['deadline']})")

                        pilih = int(input("Pilih nomor target yang ingin dihapus: "))
                        if 1 <= pilih <= len(target_bulanan):
                            target_bulanan.pop(pilih-1)
                            print("Target berhasil dihapus")
                        else:
                            print("Nomor target tidak valid!")
                    except ValueError:
                        print("Input harus angka!")

            elif pilihan == "5":
                print("program selesai, Sampai jumpa")
                break

        elif role == "member":
            if pilihan == "1":
                    nama = input("Masukkan target baru: ")
                    deadline = input("Masukkan deadline target (contoh: 30 September 2025): ")
                    target_bulanan.append({
                        "nama": nama,
                        "progress": 0,
                        "deadline": deadline
                    })
                    print("Target berhasil ditambahkan!")

            if pilihan == "2":
                if not target_bulanan:
                    print("Belum ada target untuk diupdate")
                else:
                    try:
                        print("=== Daftar Target ===")
                        for i, target in enumerate(target_bulanan, start=1):
                            print(f"{i}. {target['nama']} - {target['progress']}% (Deadline: {target['deadline']})")

                        pilih = int(input("Pilih nomor target yang ingin diupdate: "))
                        if 1 <= pilih <= len(target_bulanan):
                            progress_baru = int(input("Masukkan progress baru (0-100): "))
                    
                        else:
                            print("Nomor target tidak valid!")
                    except ValueError:
                        print("Input harus angka!")

            elif pilihan == "3":
                print("Program selesai, Sampai jumpa")
                break
            else:
                print("Pilihan tidak valid")

role = login()
if role:
    menu(role)
