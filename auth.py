from keycloak import KeycloakOpenID

# Initialize Keycloak
keycloak_openid = KeycloakOpenID(server_url="http://localhost:8080/auth/",
                                 client_id="your-client-id",
                                 realm_name="your-realm-name",
                                 client_secret_key="your-client-secret")

# Function to verify token
def verify_token(token):
    return keycloak_openid.decode_token(token)
