import hashlib

def get_hash_sha256(input: str) -> str:
    return hashlib.sha256(input.encode()).hexdigest()