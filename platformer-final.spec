# -*- mode: python -*-

block_cipher = None


a = Analysis(['platformer-final.py'],
             pathex=['G:\\My Drive\\High School\\10th Grade\\CP - 1\\platformer-final-template-animated'],
             binaries=[],
             datas=[("assets", "assets")],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='Alein Run',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )
