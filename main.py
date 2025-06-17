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
