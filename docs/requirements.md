# Velzz FTMS — Requirements M3

## 1. Tujuan Proyek

Velzz FTMS (FAST Tournament Management System) merupakan aplikasi web
untuk mendukung pengelolaan turnamen Free Fire.

## 2. Ruang Lingkup

Proyek berfokus pada inisiasi arsitektur dan deployment awal aplikasi
web pada VPS Ubuntu Server 24.04 LTS.

Mode permainan yang menjadi ruang lingkup:
- Clash Squad (CS).
- Battle Royale (BR).

## 3. Kebutuhan Fungsional

- FR-01: Sistem menampilkan halaman utama Velzz FTMS.
- FR-02: Halaman utama menampilkan informasi mode Clash Squad dan
  Battle Royale.
- FR-03: Sistem menyediakan endpoint /health untuk memeriksa kesehatan
  aplikasi.
- FR-04: Endpoint /health mengembalikan HTTP 200 dan status JSON "ok".

## 4. Kebutuhan Nonfungsional

- NFR-01: Aplikasi berjalan pada Ubuntu Server 24.04 LTS.
- NFR-02: Aplikasi menggunakan Flask dan Gunicorn.
- NFR-03: systemd mengelola proses aplikasi.
- NFR-04: Caddy bertindak sebagai reverse proxy HTTP.
- NFR-05: UFW mengatur akses jaringan pada VPS.
- NFR-06: Port aplikasi Gunicorn hanya dapat diakses melalui localhost
  pada alamat 127.0.0.1:8000.
- NFR-07: Source code dan dokumentasi disiapkan untuk dikelola melalui Git.

## 5. Batasan

- Database belum diimplementasikan.
- Docker dan Infrastructure as Code tidak termasuk M3.
- CI/CD belum diimplementasikan.
- Domain dan HTTPS/TLS belum dikonfigurasi pada M3.

## 6. Kriteria Penerimaan

- Halaman utama dapat diakses melalui HTTP.
- Endpoint /health mengembalikan HTTP 200.
- Service aplikasi dan Caddy berjalan.
- Firewall UFW aktif.
- Dokumentasi arsitektur dan deployment tersedia.
