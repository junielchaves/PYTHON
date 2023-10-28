# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['ToDo.py'],
    pathex=[],
    binaries=[],
    datas=[('assets', 'database.db')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='ToDo',
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
    version='C:\\Users\\junie\\AppData\\Local\\Temp\\85543dce-5adb-465d-8f4f-691b4fe5bd86',
    icon=['assets\\images\\favicon.ico'],
)
