from flask import Blueprint, jsonify, request
from marshmallow import ValidationError

from database.models.BotModel import Bot
from validators.bot_schema import BotSchema

bot_blueprint = Blueprint('bot_blueprint', __name__)

bot = Bot()


@bot_blueprint.route('/<bot_name>', methods=['GET'])
def get_bot(bot_name):
    try:
        bot_details = bot.get(bot_name=bot_name)
        return jsonify(bot_details), 200
    except KeyError as e:
        return jsonify({'message': "Can't find bot"}), 404
    except Exception as e:
        return jsonify({'message': str(e)}), 404

@bot_blueprint.route('/<bot_name>', methods=['DELETE'])
def delete_bot(bot_name):
    try:
        bot.delete(bot_name=bot_name)
        return '', 200
    except KeyError as e:
        return jsonify({'message': "Can't find bot"}), 404
    except Exception as e:
        return jsonify({'message': str(e)}), 404


@bot_blueprint.route('', methods=['POST'])
def create_bot():
    try:
        bot_schema = BotSchema()
        json_data = request.get_json()
        result = bot_schema.load(json_data)
        bot_name = bot.insert(new_bot=result)
        return jsonify({'message': "Bot created successfully","bot_primary_key": bot_name}), 200

    except ValidationError as e:
        return jsonify({'message': 'Validation error', 'errors': e.messages}), 400

    except Exception as e:
        return jsonify({'message': str(e)}), 404


@bot_blueprint.route('/<bot_name>', methods=['PUT'])
def update_bot(bot_name):
    try:
        bot_schema = BotSchema(partial=True)
        json_data = request.get_json()
        result = bot_schema.load(json_data)
        bot.update(bot_name=bot_name,updated_fields=result)
        return jsonify({'message': "Bot updated successfully"}), 200

    except ValidationError as e:
        return jsonify({'message': 'Validation error', 'errors': e.messages}), 400

    except Exception as e:
        return jsonify({'message': str(e)}), 404
