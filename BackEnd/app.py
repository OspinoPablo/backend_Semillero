from Routes.user_routes import users_routes
from Routes.gun_type_routes import gun_type_routes
from Routes.crime_type_routes import crime_type_routes
from Routes.report_routes import reports_routes
from db.db import app

app.register_blueprint(users_routes, url_prefix="/users")
app.register_blueprint(gun_type_routes, url_prefix="/guntipe")
app.register_blueprint(crime_type_routes, url_prefix="/crimetipe")
app.register_blueprint(reports_routes, url_prefix="/reports")

@app.route("/")
def index():
    return "Hola mundo"

if __name__ == "__main__":
    app.run(debug=True)
