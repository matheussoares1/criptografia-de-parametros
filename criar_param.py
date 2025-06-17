from cryptography.fernet import Fernet

# Carrega chave
with open("secret.key", "rb") as key_file:
    key = key_file.read()

fernet = Fernet(key)

# Texto original (o conteúdo do .ini)
original = """
[mysql]
host = localhost
user = root
password = 
database = teste
""".strip().encode()

# Criptografa e salva
encrypted = fernet.encrypt(original)
with open("param.enc", "wb") as f:
    f.write(encrypted)
