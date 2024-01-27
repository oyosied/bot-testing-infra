from marshmallow import Schema, fields, validate, validates, ValidationError

ALLOWED_INTENTS = ['play_sound', 'tell_joke', 'disconnect', 'another_intent']

class BotSchema(Schema):
    name = fields.Str(required=True, validate=validate.Length(min=1))
    url = fields.Url(required=True)
    intents = fields.List(fields.Str(), required=True, validate=validate.Length(min=1))

    @validates('intents')
    def validate_intents(self, value):
        invalid_intents = [intent for intent in value if intent not in ALLOWED_INTENTS]
        if invalid_intents:
            raise ValidationError(f"Invalid intents: {invalid_intents}. Allowed intents are: {ALLOWED_INTENTS}")
