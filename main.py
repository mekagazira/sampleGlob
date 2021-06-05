import glob
import os

#files = glob.glob('input/**/*.txt')

# 再帰的に取得する
files = glob.glob('input/**/*.txt', recursive=True)

print(files)

# パスとファイル名を取得
for f in files:
    print(os.path.split(f)[0] , end='：')
    print(os.path.split(f)[1])