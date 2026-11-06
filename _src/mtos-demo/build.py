import base64, json, os, subprocess, sys
D = os.path.dirname(os.path.abspath(__file__))
FONTDIR = os.path.join(D, 'fonts') if os.path.isdir(os.path.join(D, 'fonts')) else os.path.join(D, '..', 'fontpkg', 'package', 'dist', 'web', 'static', 'woff2')
tpl = open(os.path.join(D, 'template.html'), encoding='utf-8').read()
chars = set(tpl) | set(''.join(chr(c) for c in range(32, 127))) | set('·…⏱→›')
chars = ''.join(sorted(c for c in chars if ord(c) >= 32))
open(os.path.join(D, 'chars.txt'), 'w', encoding='utf-8').write(chars)
faces = []
for w, name in [(400, 'Regular'), (500, 'Medium'), (600, 'SemiBold'), (700, 'Bold'), (800, 'ExtraBold')]:
    src = os.path.join(FONTDIR, f'Pretendard-{name}.woff2')
    out = os.path.join(D, f'sub-{name}.woff2')
    subprocess.run([sys.executable, '-m', 'fontTools.subset', src, f'--text-file={os.path.join(D, "chars.txt")}',
                    '--flavor=woff2', f'--output-file={out}', '--layout-features=*'], check=True)
    b = base64.b64encode(open(out, 'rb').read()).decode()
    faces.append(f"@font-face{{font-family:'Pretendard';font-weight:{w};font-style:normal;font-display:block;src:url(data:font/woff2;base64,{b}) format('woff2')}}")
imgs = {}
for f in sorted(os.listdir(os.path.join(D, 'assets'))):
    k = f.rsplit('.', 1)[0]
    imgs[k] = 'data:image/webp;base64,' + base64.b64encode(open(os.path.join(D, 'assets', f), 'rb').read()).decode()
motion = json.load(open(os.path.join(D, 'motion.json'), encoding='utf-8'))
html = tpl.replace('{{FONTS}}', '\n'.join(faces)).replace('{{IMGS}}', json.dumps(imgs)).replace('{{MOTION}}', json.dumps(motion, ensure_ascii=False))
open(os.path.join(D, 'mtos-demo.html'), 'w', encoding='utf-8').write(html)
print('size', len(html.encode()))
