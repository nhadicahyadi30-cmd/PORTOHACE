"""Build dist/index.html dari src/index.src.html.
Foto diambil dari assets/foto-cutout.webp, CV PDF dari folder cv/ (tidak ikut di-commit)."""
import base64, os
R = os.path.dirname(os.path.abspath(__file__))
rd = lambda p: open(os.path.join(R, p), 'rb').read()
t = rd('src/index.src.html').decode()
t = t.replace('%%PHOTO%%', base64.b64encode(rd('assets/foto-cutout.webp')).decode())
for v in ['Maintenance', 'Automation', 'Production']:
    p = f'cv/CV_Nurahmad_Hadi_Cahyadi_{v}.pdf'
    data = base64.b64encode(rd(p)).decode() if os.path.exists(os.path.join(R, p)) else ''
    if not data: print('PERINGATAN: tidak ada', p)
    t = t.replace(f'%%CV_{v}%%', data)
os.makedirs(os.path.join(R, 'dist'), exist_ok=True)
open(os.path.join(R, 'dist/index.html'), 'w').write(t)
print('OK -> dist/index.html', len(t) // 1024, 'KB')
