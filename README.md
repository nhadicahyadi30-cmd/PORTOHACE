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

## Galeri: dokumentasi proyek, lomba, sertifikat
Foto/sertifikat disimpan di `assets/gallery/` (WebP/JPG, sekitar 100-200 KB per file) dan didaftarkan di `data/gallery.json`:
```json
{
  "p1": [ {"s": "assets/gallery/doser-1.webp", "c": "Prototipe doser", "t": "photo"} ],
  "aw-national-ships-design-and-boat-sep-2023": [
    {"s": "assets/gallery/nasdarc-1.webp", "c": "Final run", "t": "photo"},
    {"s": "assets/gallery/nasdarc-sertifikat.webp", "c": "Sertifikat", "t": "cert"}
  ],
  "c-solar-energy-bootcamp-2024": [ {"s": "assets/gallery/solar.webp", "c": "Sertifikat", "t": "cert"} ]
}
```
- Kunci `pN` = proyek, `aw-...` = penghargaan, `c-...` = sertifikat pelatihan. Daftar lengkap: `python build.py --keys`
- `t` = `photo` (dokumentasi) atau `cert` (sertifikat). Foto proyek tampil di jendela detail proyek; penghargaan dapat tombol Photos/Certificate; sertifikat pelatihan dapat tombol View certificate.
- Sertifikat: tutup nomor mahasiswa/data pribadi sebelum diunggah. Foto proyek perusahaan: pastikan boleh dipublikasikan.

## Jalankan di localhost (Windows)
Klik dua kali `jalankan.bat`: build otomatis, server jalan di http://localhost:8000 dan browser terbuka.
Manual: `python build.py`, lalu `cd dist` dan `python -m http.server 8000`.

## Catatan teknis
- Tema: `html[data-theme]`, disimpan di localStorage `enh-theme`
- Routing hash: `#about #career #projects #skills #achievements #training`
- Lanyard: Verlet physics, tali bisa mengendur, sudut card dibatasi ±1,15 rad agar tidak terbalik

## To-do
- [ ] Foto proyek
- [ ] Hasil kerja Production Engineer
- [ ] Testimoni
- [ ] Kontak WhatsApp/email (juga untuk halaman Freelance)
- [ ] Toggle ID/EN
- [ ] CV versi tanpa tanggal lahir
