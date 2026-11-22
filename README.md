# PORTOHACE — Portofolio ENHACE (Nurahmad Hadi Cahyadi)

Website portofolio satu file (HTML/CSS/JS tanpa framework): loader hitung mundur, mode gelap/terang,
ID card lanyard berfisika, mini-game kontrol lantai produksi, halaman karir, prestasi, training, proyek, dan skill.

## Struktur
- `src/index.src.html` — sumber utama (template, placeholder `%%PHOTO%%` dan `%%CV_*%%`)
- `assets/foto-cutout.webp` — foto ID card (background transparan)
- `cv/` — taruh PDF CV di sini (tidak di-commit karena memuat data pribadi)
- `build.py` — menggabungkan semuanya ke `dist/index.html`
- `docs/` — dokumentasi proyek (diisi bertahap)

## Build
```
python3 build.py
```
Nama file CV: `cv/CV_Nurahmad_Hadi_Cahyadi_{Maintenance,Automation,Production}.pdf`

## Jalankan di localhost (Windows)
Klik dua kali `jalankan.bat`: build otomatis, server jalan di http://localhost:8000 dan browser terbuka.
Manual: `python build.py`, lalu `cd dist` dan `python -m http.server 8000`.

## Catatan teknis
- Tema: `html[data-theme]`, disimpan di localStorage `enh-theme`
- Routing hash: `#about #career #projects #skills #achievements #training`
- Lanyard: Verlet physics, tali bisa mengendur, sudut card dibatasi ±1,15 rad agar tidak terbalik

## To-do
- [ ] Ganti Achievements dengan Education, lalu buat Achievements baru dari LinkedIn (sempat dicoba lalu dikembalikan)
- [ ] Foto proyek
- [ ] Hasil kerja Production Engineer
- [ ] Testimoni
- [ ] Kontak WhatsApp/email
- [ ] Toggle ID/EN
- [ ] CV versi tanpa tanggal lahir
