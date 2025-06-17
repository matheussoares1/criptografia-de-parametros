✅ 1. Opção leve: Criptografia com chave simétrica (Fernet)
Você pode criptografar o conteúdo do param.ini com uma chave secreta e descriptografar no momento da execução.

🔐 Instalar a biblioteca:
```bash
pip install cryptography
```
🧩 Passo 1: Gerar a chave secreta (só uma vez)
python
Copiar
Editar
```python
from cryptography.fernet import Fernet

key = Fernet.generate_key()
with open("secret.key", "wb") as key_file:
    key_file.write(key)

```
🧩 Passo 2: Criar o param.enc (criptografado)
Você vai criptografar o conteúdo do .ini como string:

```python
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

```
🧩 Passo 3: Ler e descriptografar no seu código principal
Atualize a função conectar():

```python

import mysql.connector
from datetime import datetime
import configparser
from cryptography.fernet import Fernet

def carregar_config():
    # Carrega a chave
    with open("secret.key", "rb") as key_file:
        key = key_file.read()
    fernet = Fernet(key)

    # Lê e descriptografa o arquivo
    with open("param.enc", "rb") as enc_file:
        encrypted_data = enc_file.read()

    decrypted_data = fernet.decrypt(encrypted_data).decode()

    # Carrega como se fosse um .ini
    config = configparser.ConfigParser()
    config.read_string(decrypted_data)
    return config

def conectar():
    config = carregar_config()
    return mysql.connector.connect(
        host=config['mysql']['host'],
        user=config['mysql']['user'],
        password=config['mysql']['password'],
        database=config['mysql']['database']
    )

```
🔒 Segurança real: Onde guardar a chave (secret.key)?
NUNCA coloque ela no mesmo repositório do código, principalmente se usar Git.

Em produção, salve:

Em uma variável de ambiente;

Em um cofre de segredos (como AWS Secrets Manager, HashiCorp Vault, etc.).
