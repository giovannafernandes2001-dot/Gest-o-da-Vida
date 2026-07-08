import pathlib
tpl = pathlib.Path('gestao-da-vida-preview.template.html').read_text()
fonts = pathlib.Path('fonts'); f2 = pathlib.Path('fonts2'); f3 = pathlib.Path('fonts3')
k2 = pathlib.Path('kittl2')
video = pathlib.Path('video')
repl = {
    '__INTRO_MP4__': (video/'intro.b64').read_text().strip(),
    '__INTRO_WEBM__': (video/'intro-webm.b64').read_text().strip(),
    '__GILDA__': (f2/'gilda-display.b64').read_text().strip(),
    '__CORMORANT_REG__': (f2/'cormorant-garamond.b64').read_text().strip(),
    '__CORMORANT_ITALIC__': (f3/'cormorant-italic.b64').read_text().strip(),
    '__KARLA__': (fonts/'karla.b64').read_text().strip(),
    '__SPACEMONO_400__': (f3/'space-mono-400.b64').read_text().strip(),
    '__SPACEMONO_700__': (f3/'space-mono-700.b64').read_text().strip(),
    '__ICON_GREEN__': (k2/'mark-icon-green.b64').read_text().strip(),
    '__ICON_CREAM__': (k2/'mark-icon-cream.b64').read_text().strip(),
    '__COMPASS_GREEN__': (k2/'compass-green-gold.b64').read_text().strip(),
    '__COMPASS_DARK__': (k2/'compass-dark-theme.b64').read_text().strip(),
    '__TILE_GREEN__': (k2/'mark-tile-green-white.b64').read_text().strip(),
}
for k, v in repl.items():
    assert k in tpl, f'missing {k}'
    tpl = tpl.replace(k, v)
pathlib.Path('gestao-da-vida-preview.html').write_text(tpl)
print('ok', len(tpl))
