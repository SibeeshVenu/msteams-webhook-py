from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
import logging
logging.basicConfig(level=logging.INFO)


def get_key_vault_secret(key_vault_name: str, secret_name: str):
    try:
        # Authenticate and securely retrieve azure credentials
        key_vault_uri = f'https://{key_vault_name}.vault.azure.net'
        #az_credential = DefaultAzureCredential()
        az_credential = DefaultAzureCredential(
            exclude_visual_studio_code_credential=True,
            exclude_shared_token_cache_credential=True,
            exclude_managed_identity_credential=True,
            exclude_environment_credential=True,
            exclude_cli_credential=False
        )
        secret_client = SecretClient(
            vault_url=key_vault_uri, credential=az_credential)
        access_key_secret = secret_client.get_secret(secret_name)
        logging.info('Successfully returned the secret from the Key Vault!')
        return access_key_secret
    except Exception as e:
        logging.error(
            f'get_key_vault_secret: Error getting key vault secret: {e}')
        return None
