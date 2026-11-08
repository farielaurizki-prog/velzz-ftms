# Velzz FTMS

Velzz FTMS (FAST Tournament Management System) adalah proyek web untuk mendukung pengelolaan turnamen Free Fire.

## Ruang Lingkup

- Clash Squad (CS): mode pertandingan berbasis ronde.
- Battle Royale (BR): mode permainan bertahan hidup.

## Teknologi

- Python dan Flask
- Gunicorn
- Caddy
- Ubuntu Server 24.04 LTS
- systemd

## Arsitektur

Browser mengirimkan HTTP request ke Caddy pada port 80.
Caddy meneruskan request ke Gunicorn pada 127.0.0.1:8000.
Gunicorn menjalankan aplikasi Flask.

## Menjalankan Aplikasi

Aktifkan virtual environment dan instal dependensi:

    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt

Jalankan aplikasi untuk pengembangan:

    flask --app app run

Buka http://127.0.0.1:5000 di browser.

## Endpoint

- / : halaman utama.
- /health : endpoint pemeriksaan kesehatan yang mengembalikan HTTP 200.
- /api/info : endpoint informasi aplikasi yang mengembalikan JSON dan HTTP 200.
## Deployment M3

Aplikasi dideploy pada VPS Ubuntu Server 24.04 LTS menggunakan Gunicorn, systemd, dan Caddy.

Alamat deployment: http://16.178.214.220

Deployment ini menggunakan HTTP melalui alamat IP publik. Domain dan HTTPS belum dikonfigurasi.

## Batasan M3

Fokus tahap ini adalah arsitektur awal dan deployment VPS.
Database, Docker, CI/CD, Infrastructure as Code, domain produksi, dan TLS belum termasuk ruang lingkup.


## Struktur Proyek

    velzz-ftms/
    ├── app.py
    ├── requirements.txt
    ├── .env.example
    ├── .gitignore
    ├── README.md
    ├── templates/
    │   └── index.html
    ├── static/
    │   └── style.css
    └── docs/
        ├── requirements.md
        ├── architecture.md
        ├── deployment.md
        ├── adr/
        └── evidence/
            ├── m03/
            └── ev03-riset-pengguna.md


## Dokumentasi Praktikum M03

- [Requirements](docs/requirements.md)
- [Arsitektur Sistem](docs/architecture.md)
- [Panduan Deployment](docs/deployment.md)
- [ADR-0001](docs/adr/0001-initial-architecture.md)
- [Evidence Deployment M03](docs/evidence/m03/)
- [Evidence Riset Pengguna](docs/evidence/ev03-riset-pengguna.md)

## Pengelolaan Proyek

- [GitHub Issues](https://github.com/farielaurizki-prog/velzz-ftms/issues)
- [GitHub Releases](https://github.com/farielaurizki-prog/velzz-ftms/releases)

## Status Praktikum M03

- Aplikasi Flask berhasil dideploy pada AWS EC2.
- Gunicorn, systemd, dan Caddy telah dikonfigurasi.
- Firewall UFW dan SSH hardening telah diterapkan.
- Endpoint /health dan /api/info berhasil diuji.
- Dokumentasi dan evidence tersedia di GitHub.

