from keycloak import KeycloakOpenID, KeycloakAdmin
from django.conf import settings

keycloak_admin = KeycloakAdmin(
    server_url=settings.KEYCLOAK_SERVER_URL,
    username=settings.KEYCLOAK_ADMIN_USERNAME,
    password=settings.KEYCLOAK_ADMIN_PASSWORD,
    client_id=settings.KEYCLOAK_CLIENT_ID,
    realm_name=settings.KEYCLOAK_REALM_NAME,
    verify=True
)

keycloak_openid = KeycloakOpenID(
    server_url=settings.KEYCLOAK_SERVER_URL,
    client_id=settings.KEYCLOAK_CLIENT_ID,
    realm_name=settings.KEYCLOAK_REALM_NAME
)


def create_user_in_keycloak(username, email, first_name, last_name, password, roles):
    user_id = keycloak_admin.create_user({
        "username": username,
        "email": email,
        "firstName": first_name,
        "lastName": last_name,
        "enabled": True,
        "credentials": [{"value": password, "type": "password"}]
    })

    for role in roles:
        keycloak_admin.assign_client_role(client_id=keycloak_admin.get_client_id(settings.KEYCLOAK_CLIENT_ID),
                                          user_id=user_id, roles=[{"name": role}])

    return user_id


def authenticate_user(username, password):
    try:
        token = keycloak_openid.token(username, password)
        return token
    except Exception as e:
        raise PermissionError(f"Authentication failed: {str(e)}")
    

def get_userinfo(token):
    return keycloak_openid.userinfo(token['access_token'])


def verify_role(token, required_role):
    userinfo = get_userinfo(token)
    roles = userinfo.get('realm_access', {}).get('roles', [])
    return required_role in roles