from datetime import datetime

def hitung_umur_dan_hari():
    print("=== PROGRAM MENGHITUNG UMUR & HARI LAHIR ===")
    
    try:
        tahun_lahir = int(input("Masukkan Tahun Lahir (YYYY) : "))
        bulan_lahir = int(input("Masukkan Bulan Lahir (1-12) : "))
        tanggal_lahir = int(input("Masukkan Tanggal Lahir (1-31): "))
     
        tgl_lahir = datetime(tahun_lahir, bulan_lahir, tanggal_lahir)
        
        tgl_sekarang = datetime.now()
        
        if tgl_lahir > tgl_sekarang:
            print("\n[Error] Tanggal lahir tidak boleh lebih besar dari hari ini!")
            return

        tahun = tgl_sekarang.year - tgl_lahir.year
        bulan = tgl_sekarang.month - tgl_lahir.month
        hari = tgl_sekarang.day - tgl_lahir.day
        
        if hari < 0:
            bulan -= 1

            bulan_sebelumnya = tgl_sekarang.month - 1 if tgl_sekarang.month > 1 else 12
            tahun_sebelumnya = tgl_sekarang.year if tgl_sekarang.month > 1 else tgl_sekarang.year - 1
            
            from calendar import monthrange
            _, jumlah_hari = monthrange(tahun_sebelumnya, bulan_sebelumnya)
            hari += jumlah_hari
            
        if bulan < 0:
            tahun -= 1
            bulan += 12

        daftar_hari = {
            'Monday': 'Senin',
            'Tuesday': 'Selasa',
            'Wednesday': 'Rabu',
            'Thursday': 'Kamis',
            'Friday': 'Jumat',
            'Saturday': 'Sabtu',
            'Sunday': 'Minggu'
        }
        
        nama_hari_en = tgl_lahir.strftime('%A')
        nama_hari_id = daftar_hari.get(nama_hari_en, nama_hari_en)

        print("\n" + "="*40)
        print(f"Hari Lahir Anda : {nama_hari_id}, {tgl_lahir.strftime('%d-%m-%Y')}")
        print(f"Usia Anda Saat Ini: {tahun} tahun, {bulan} bulan, {hari} hari")
        print("="*40)

    except ValueError:
        print("\n[Error] Masukan data tidak valid! Harap masukkan angka yang benar.")
        
hitung_umur_dan_hari()