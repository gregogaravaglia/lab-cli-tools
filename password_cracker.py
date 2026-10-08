from zipfile import ZipFile, BadZipFile
import zlib

# Step 1: build a list of every candidate password in the file.
with open('Ashley-Madison.txt', 'r', encoding='latin-1') as f:
    passwords = [line.strip() for line in f]

# Step 2: try each password until the zip opens.
for count, password in enumerate(passwords):
    # progress line every 10,000 tries so we can see it is still moving
    if count % 10000 == 0:
        print(count, password)
    try:
        with ZipFile('whitehouse_secrets.zip') as zf:
            zf.extractall(pwd=password.encode())
        # if we get here, extraction succeeded
        print('SUCCESS! The password is:', password)
        break
    except (RuntimeError, BadZipFile, zlib.error):
        # wrong password: skip it and try the next one
        continue
