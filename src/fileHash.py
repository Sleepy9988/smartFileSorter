import hashlib

def createHash(file):
    BUF_SIZE = 65536

    sha256 = hashlib.sha256()
    try:
        with open(str(file), 'rb') as f:
            while chunk := f.read(BUF_SIZE):
                sha256.update(chunk)
        return sha256.hexdigest()
    except (PermissionError, OSError):
        return "HASH_FAILED"

