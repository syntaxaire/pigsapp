# -*- mode: python -*-

block_cipher = None


a = Analysis(['PigsApp.py'],
             pathex=['C:\\Users\\Jeff\\Dropbox\\Code\\Python\\pass-the-pigs'],
             binaries=[],
             datas=[('pig_nose.ico', '.'),
                    ('pig-nose-16x16.png', '.'),
                    ('pig-nose-24x24.png', '.'),
                    ('pig-nose-32x32.png', '.'),
                    ('pig-nose-48x48.png', '.'),
                    ('pig-nose-256x256.png', '.'),
                     ],
             hiddenimports=['Player'],
             hookspath=[],
             runtime_hooks=[],
             excludes=['strategies'],
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
          name='PigsApp',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False,
          icon='pig_nose.ico' )
