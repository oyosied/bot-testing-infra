from pathlib import Path

current_script_path = Path(__file__).resolve()
ROOT_PATH = current_script_path.parent.parent
CONFIG_FILE = 'automation_infra\\infra\\utils\\config.json'
ALLOWED_INTENTS = ['play_sound', 'tell_joke', 'disconnect', 'another_intent']
