# Velzz FTMS — Deployment M3

## 1. Informasi Server

- Operating system: Ubuntu Server 24.04 LTS
- Application framework: Flask
- Application server: Gunicorn
- Process manager: systemd
- Reverse proxy: Caddy
- Firewall: UFW

## 2. Alamat Aplikasi

Alamat publik M3:

http://16.178.214.220

## 3. Struktur Layanan

- Flask dijalankan oleh Gunicorn.
- Gunicorn mendengarkan pada 127.0.0.1:8000.
- systemd mengelola service velzz-ftms.
- Caddy menerima HTTP pada port 80 dan meneruskan request
  ke Gunicorn.

## 4. Menjalankan dan Memeriksa Service

Periksa status aplikasi:

    sudo systemctl status velzz-ftms --no-pager

Periksa status Caddy:

    sudo systemctl status caddy --no-pager

Periksa firewall:

    sudo ufw status verbose

## 5. Pengujian Endpoint

Periksa health endpoint dari VPS:

    curl -i http://127.0.0.1:8000/health

Periksa aplikasi melalui Caddy:

    curl -i http://127.0.0.1/health

Response yang diharapkan adalah HTTP 200 dengan JSON:

    {"status":"ok"}

### Pengujian API Info

Periksa endpoint informasi aplikasi melalui Caddy:

    curl -i http://127.0.0.1/api/info

Hasil pengujian:
- HTTP Status: 200 OK
- Reverse Proxy: Caddy
- Application Server: Gunicorn

Response JSON:

    {"application":"Velzz FTMS","code":"PTI 2802","course":"Cloud Computing","deployment":"AWS EC2 Ubuntu 24.04","status":"ok"}

## 6. Restart dan Log

Restart aplikasi:

    sudo systemctl restart velzz-ftms

Lihat log aplikasi:

    sudo journalctl -u velzz-ftms -n 50 --no-pager

Lihat log Caddy:

    sudo journalctl -u caddy -n 50 --no-pager

## 7. Firewall

UFW digunakan untuk mengizinkan SSH pada port 22 dan HTTP pada
port 80. Port aplikasi Gunicorn 8000 tidak dibuka untuk publik.

## 8. Batasan M3

Deployment masih menggunakan HTTP melalui IP publik. Domain dan
HTTPS/TLS akan ditangani pada tahap berikutnya.

