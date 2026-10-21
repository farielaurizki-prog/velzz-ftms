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
