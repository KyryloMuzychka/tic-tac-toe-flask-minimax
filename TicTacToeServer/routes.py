from flask import Blueprint, request, jsonify, session
from db import DB

db_manager = DB()

routes = Blueprint("routes", __name__)

@routes.route("/register", methods=["POST"])
def register():
    data = request.json
    login = data.get("login")
    password = data.get("password")
    if db_manager.register_player(login, password):
        session["user"] = login
        return jsonify({"status": "success", "message": "User registered successfully"}), 201
    else:
        return jsonify({"status": "fail", "message": "Username already exists"}), 400

@routes.route("/login", methods=["POST"])
def login():
    data = request.json
    login = data.get("login")
    password = data.get("password")
    if db_manager.login(login, password):
        session["user"] = login
        return jsonify({"status": "success", "message": "Login successful"}), 200
    else:
        return jsonify({"status": "fail", "message": "Invalid data"}), 400

@routes.route("/get_player_info", methods=["GET"])
def get_player_info():
    if "user" not in session:
        return jsonify({"status": "fail", "message": "User not logged in"}), 401

    player_info = db_manager.get_player_info(session["user"])
    if player_info:
        return jsonify({"status": "success", "player_info": player_info}), 200
    else:
        return jsonify({"status": "fail", "message": "Failed to retrieve player info"}), 400

@routes.route("/update_login", methods=["PUT"])
def update_login():
    if "user" not in session:
        return jsonify({"status": "fail", "message": "User not logged in"}), 401

    data = request.json
    new_login = data.get("new_login")
    if db_manager.update_login(session["user"], new_login):
        session["user"] = new_login
        return jsonify({"status": "success", "message": "Login updated successfully"}), 200
    else:
        return jsonify({"status": "fail", "message": "Failed to update login"}), 400

@routes.route("/update_password", methods=["PUT"])
def update_password():
    if "user" not in session:
        return jsonify({"status": "fail", "message": "User not logged in"}), 401

    data = request.json
    new_password = data.get("new_password")
    if db_manager.update_password(session["user"], new_password):
        return jsonify({"status": "success", "message": "Password updated successfully"}), 200
    else:
        return jsonify({"status": "fail", "message": "Failed to update password"}), 400

@routes.route("/update_wins", methods=["PUT"])
def update_wins():
    if "user" not in session:
        return jsonify({"status": "fail", "message": "User not logged in"}), 401

    data = request.json
    wins = data.get("wins")
    if db_manager.update_wins(session["user"], wins):
        return jsonify({"status": "success", "message": "Wins updated successfully"}), 200
    else:
        return jsonify({"status": "fail", "message": "Failed to update wins"}), 400

@routes.route("/update_losses", methods=["PUT"])
def update_losses():
    if "user" not in session:
        return jsonify({"status": "fail", "message": "User not logged in"}), 401

    data = request.json
    losses = data.get("losses")
    if db_manager.update_losses(session["user"], losses):
        return jsonify({"status": "success", "message": "Losses updated successfully"}), 200
    else:
        return jsonify({"status": "fail", "message": "Failed to update losses"}), 400

@routes.route("/update_draws", methods=["PUT"])
def update_draws():
    if "user" not in session:
        return jsonify({"status": "fail", "message": "User not logged in"}), 401

    data = request.json
    draws = data.get("draws")
    if db_manager.update_draws(session["user"], draws):
        return jsonify({"status": "success", "message": "Draws updated successfully"}), 200
    else:
        return jsonify({"status": "fail", "message": "Failed to update draws"}), 400

@routes.route("/soft_delete", methods=["PUT"])
def soft_delete():
    if "user" not in session:
        return jsonify({"status": "fail", "message": "User not logged in"}), 401
        
    if db_manager.soft_delete_player(session["user"]):
        return jsonify({"status": "success", "message": "Player soft deleted successfully"}), 200
    else:
        return jsonify({"status": "fail", "message": "Failed to soft delete player"}), 400

@routes.route("/top_players", methods=["GET"])
def top_players():
    top_players = db_manager.get_top_players()
    if top_players is not None:
        return jsonify({"status": "success", "message": top_players}), 200
    else:
        return jsonify({"status": "fail", "message": "Failed to retrieve top players"}), 400

@routes.route("/get_player_rank", methods=["GET"])
def get_player_rank():
    if "user" not in session:
        return jsonify({"status": "fail", "message": "User not logged in"}), 401

    rank = db_manager.get_player_rank(session["user"])
    if rank is not None:
        return jsonify({"status": "success", "message": rank}), 200
    else:
        return jsonify({"status": "fail", "message": "Failed to retrieve player rank"}), 400
