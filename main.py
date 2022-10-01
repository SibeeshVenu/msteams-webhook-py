from notify_teams import notify_to_teams
from keyvault_helper import get_key_vault_secret

kv_secret_name = ''
kv_name = ''
web_hook_url = get_key_vault_secret(kv_name, kv_secret_name)


message = 'Hi, this message is from the Python application that uses the Webhook connector.'
notify_to_teams(message, web_hook_url.value, kv_secret_name)
