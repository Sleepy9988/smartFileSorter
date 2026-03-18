import hashlib

def createHash(file):
    BUF_SIZE = 65536

    sha256 = hashlib.sha256()

    with open(file, 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)

            if not data:
                break 
            sha256.update(data)

    return sha256.hexdigest()


