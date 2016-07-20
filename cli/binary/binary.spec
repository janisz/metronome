# -*- mode: python -*-

block_cipher = None


a = Analysis(['../dcos_metronome/cli.py'],
             pathex=[os.getcwd(), 'env/lib/python2.7/site-packages'],
             binaries=None,
             datas=[('../dcos_metronome/data/config-schema/*', 'dcos_metronome/data/config-schema')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='dcos-job',
          debug=False,
          strip=False,
          upx=True,
          console=True )