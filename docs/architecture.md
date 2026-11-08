# Velzz FTMS — Architecture M3

## Gambaran Umum

Velzz FTMS menggunakan Flask sebagai backend, Gunicorn sebagai
application server, dan Caddy sebagai reverse proxy HTTP.

## Alur Request

1. Browser mengakses VPS melalui HTTP port 80.
2. Caddy menerima request.
3. Caddy meneruskan request ke Gunicorn di 127.0.0.1:8000.
4. Gunicorn menjalankan aplikasi Flask.
5. Flask mengirimkan response kepada browser.

## Komponen

- Flask: aplikasi web.
- Gunicorn: menjalankan Flask.
- Caddy: reverse proxy.
- systemd: mengelola service aplikasi.
- UFW: mengatur firewall VPS.

## Endpoint

- `/`: halaman utama Velzz FTMS.
- `/health`: pemeriksaan kesehatan aplikasi.

## Keamanan

Gunicorn hanya mendengarkan pada 127.0.0.1:8000.
Port 8000 tidak dibuka untuk akses publik.
Website M3 masih menggunakan HTTP melalui IP publik.

## Infrastruktur Cloud

Aplikasi Velzz FTMS pada Praktikum M03 dijalankan
menggunakan AWS EC2 dengan Ubuntu Server 24.04 LTS.

Komponen deployment:
- Cloud Provider: Amazon Web Services (AWS).
- Compute Service: Amazon EC2.
- Instance Type: t3.micro.
- Operating System: Ubuntu Server 24.04 LTS.
- Web Server / Reverse Proxy: Caddy.
- Application Server: Gunicorn.
- Backend Framework: Flask.
- Service Manager: systemd.
- Firewall: UFW.

## Endpoint Tambahan

- `/api/info`: menampilkan informasi aplikasi Velzz FTMS
  dalam format JSON dengan respons HTTP 200 OK.

## Keamanan SSH

- Akses SSH menggunakan autentikasi public key.
- Autentikasi SSH menggunakan password dinonaktifkan.
- Login SSH sebagai root dinonaktifkan.
- Gunicorn hanya menerima koneksi melalui localhost.
