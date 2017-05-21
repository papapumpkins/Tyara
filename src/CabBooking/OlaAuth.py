import requests
import httplib2

client_id = "ODVlMGVkOTEtMjc2Zi00YmY3LThmMDAtNTQ2ZDFkMGRiMGY2"
redirect_uri= "http://localhost/ola/tokens"
OAuth_uri= "https://sandbox-1.olacabs.com/oauth2/authorizeresponse_type=token&client_id=ODVlMGVkOTEtMjc2Zi00YmY3LThmMDAtNTQ2ZDFkMGRiMGY2&redirect_uri=http://localhost/ola/tokens&scope=profile%20booking&state=state123"
OAuth_uri2="https://devapi.olacabs.com/oauth2/authorize?response_type=token&client_id="+client_id+"&redirect_uri="+redirect_uri+"&scope=profile%20booking"
XApp_token="3621fa8e13354829b06d0fb3ae187faa"

def get_auth_token():
    token_request = requests.get(OAuth_uri2)
    print(str(token_request))

get_auth_token()