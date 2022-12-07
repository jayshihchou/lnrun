# flake8: noqa
from .send_message import (send_message, main as _send_message_cli)
from .send_image import (send_image, main as _send_image_cli)
from .config import load_config, write_config, get_token, is_token_setted
from .run import main as _run_main_cli
from .get_configs import main as _get_configs_cli
from .set_config import main as _set_config_cli

