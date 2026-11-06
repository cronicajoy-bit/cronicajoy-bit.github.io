# M-TOS 홈 시연 — 소스

- 공개 주소: https://cronicajoy-bit.github.io/mtos-demo-k7r4/
- 피그마: 5JhgQrdm6cqbpzB2N9XbuX (라임 통일 화면 275:912, 275:1280, 275:1668, 275:2062, 275:2437 / 주문내역 309:2069)

## 갱신 순서
1. `template.html` 수정 (모션은 `motion.json`, 이미지는 `assets/`)
2. `python3 build.py` → `mtos-demo.html` (claude.ai 아티팩트용)
3. `python3 mkstand.py` → `../../mtos-demo-k7r4/index.html` (공개 주소용)
4. 커밋·푸시하면 1~2분 뒤 반영

`_`로 시작하는 폴더라 웹에는 공개되지 않아요(GitHub Pages가 제외).
