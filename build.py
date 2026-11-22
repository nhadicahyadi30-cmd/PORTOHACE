"""Build dist/index.html dari src/index.src.html.
- Foto ID card : assets/foto-cutout.webp
- CV PDF       : cv/ (tidak ikut di-commit)
- Galeri       : data/gallery.json + file gambar di assets/gallery/ (disalin ke dist/)
Jalankan `python build.py --keys` untuk melihat daftar kunci galeri."""
import base64, os, re, shutil, sys, json
R = os.path.dirname(os.path.abspath(__file__))
rd = lambda p: open(os.path.join(R, p), 'rb').read()
src = rd('src/index.src.html').decode()

if '--keys' in sys.argv:
    print('# Kunci galeri (pakai di data/gallery.json)\n')
    for k, y, t in re.findall(r'"k": "(aw-[^"]+)",\s*"y": "([^"]+)",\s*"r": "[^"]*",\s*"t": "([^"]+)"', src):
        print(f'{k}  {y} | {t}')
    print()
    for k, y, t in re.findall(r'\{k:"(c-[^"]+)",y:"([^"]+)",t:"([^"]+)"', src):
        print(f'{k}  {y} | {t}')
    print()
    for i, t in re.findall(r'\{id:(\d+),t:"([^"]+)"', src):
        print(f'p{i}  {t}')
    sys.exit()

t = src
t = t.replace('%%PHOTO%%', base64.b64encode(rd('assets/foto-cutout.webp')).decode())
for v in ['Maintenance', 'Automation', 'Production']:
    p = f'cv/CV_Nurahmad_Hadi_Cahyadi_{v}.pdf'
    data = base64.b64encode(rd(p)).decode() if os.path.exists(os.path.join(R, p)) else ''
    if not data: print('PERINGATAN: tidak ada', p)
    t = t.replace(f'%%CV_{v}%%', data)
gal = json.loads(rd('data/gallery.json').decode() or '{}') if os.path.exists(os.path.join(R, 'data/gallery.json')) else {}
t = t.replace('%%GALLERY%%', json.dumps(gal, ensure_ascii=False))
for k, items in gal.items():
    for it in items:
        if not os.path.exists(os.path.join(R, it['s'])): print(f'PERINGATAN: file tidak ada: {it["s"]} ({k})')
os.makedirs(os.path.join(R, 'dist'), exist_ok=True)
open(os.path.join(R, 'dist/index.html'), 'w').write(t)
g = os.path.join(R, 'assets/gallery')
if os.path.isdir(g):
    d = os.path.join(R, 'dist/assets/gallery')
    shutil.rmtree(d, ignore_errors=True); shutil.copytree(g, d)
print('OK -> dist/index.html', len(t) // 1024, 'KB')
