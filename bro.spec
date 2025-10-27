# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['bro.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='bro',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['/Users/mr.quant/Downloads/OIP.QSbFRI1RbIta1AxRhx8riwHaHa.jpeg'],
)
app = BUNDLE(
    exe,
    name='bro.app',
    icon='/Users/mr.quant/Downloads/OIP.QSbFRI1RbIta1AxRhx8riwHaHa.jpeg',
    bundle_identifier=None,
)
