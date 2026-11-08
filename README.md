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

## Deployment M3

Aplikasi dideploy pada VPS Ubuntu Server 24.04 LTS menggunakan Gunicorn, systemd, dan Caddy.

Alamat deployment: http://52.65.125.172

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

