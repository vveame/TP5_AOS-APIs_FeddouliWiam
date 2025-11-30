from flask import Flask, jsonify
from config import Config
import pymysql
from extensions import db


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    DB_USER = Config.DB_USER
    DB_PASS = Config.DB_PASSWORD
    DB_HOST = Config.DB_HOST
    DB_PORT = Config.DB_PORT
    DB_NAME = Config.DB_NAME

    conn = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASS, port=DB_PORT)
    cursor = conn.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
    cursor.close()
    conn.close()

    db.init_app(app)

    with app.app_context():
        from entity.filiere import Filiere
        db.create_all()

    # register blueprints
    from web.filiere_controller import bp as filiere_bp
    app.register_blueprint(filiere_bp)

    # simple root and health endpoints
    @app.route("/")
    def root():
        return jsonify({"app": Config.APP_NAME})

    @app.route("/actuator/health")
    def health():
        return jsonify({"status": "UP"})

    return app


if __name__ == "__main__":
    from eureka_client import start_eureka_client
    start_eureka_client()
    app = create_app()
    app.run(host="0.0.0.0", port=Config.APP_PORT)
