from flask import Blueprint


# Import sub routes
from routes.user_routes import user_bp
#from routes.account_routes import account_bp


blueprints = [
    user_bp,
#    account_bp,
]