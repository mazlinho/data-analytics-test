from tangany_settlement_api_sdk import SettlementClient
from tangany_settlement_api_sdk.auth import Credentials

credentials = Credentials(client_id="_will_be_provided_", client_secret="_will_be_provided_")
api = SettlementClient(credentials=credentials)

assets = api.assets.list() 
print(assets)
