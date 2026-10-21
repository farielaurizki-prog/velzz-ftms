# ADR-0001: Initial Architecture

- Status: Accepted
- Date: 2026-10-21

## Context

Velzz FTMS memerlukan aplikasi web awal yang dapat diakses melalui
internet dan dideploy pada VPS Ubuntu Server 24.04 LTS.

Pada M3, fokus proyek adalah arsitektur awal dan first deployment.
Database, Docker, CI/CD, dan Infrastructure as Code belum menjadi
bagian dari ruang lingkup.

## Decision

Komponen yang dipilih:

- Flask sebagai web framework.
- Gunicorn sebagai application server.
- systemd untuk mengelola service aplikasi.
- Caddy sebagai reverse proxy HTTP.
- UFW sebagai firewall server.
- Git untuk version control source code.

Gunicorn berjalan pada 127.0.0.1:8000. Caddy menerima HTTP melalui
port 80 dan meneruskan request ke Gunicorn.

## Consequences

### Positive

- Arsitektur sederhana dan mudah dipahami.
- Service aplikasi dapat dikelola menggunakan systemd.
- Backend tidak perlu diekspos langsung ke internet.
- Konfigurasi dapat dikembangkan pada tahap berikutnya.

### Trade-offs

- Website M3 masih menggunakan HTTP.
- Belum ada database atau pipeline CI/CD.
- Deployment dan pengujian masih dilakukan secara manual.

## Future Considerations

Konfigurasi domain, DNS, dan HTTPS/TLS akan dievaluasi pada M4.
