from flask import Flask, render_template
from flask_graphql import GraphQLView
from flask_graphql_auth import GraphQLAuth
from schema import schema
from auth import keycloak

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# Initialize Flask-GraphQL-Auth
auth = GraphQLAuth(app)

# Register Keycloak authentication
auth.register_keycloak(keycloak)

# GraphQL endpoint
app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

# Basic UI route
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
