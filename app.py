import os
import logging

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

from functions import grammar_suggestion

# Initialization
app = App(token=os.environ.get("SLACK_BOT_TOKEN"))
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] [%(filename)s:%(lineno)d] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

# Register Function
app.function("grammar_suggestion")(grammar_suggestion)

# Start Bolt app
if __name__ == "__main__":
    SocketModeHandler(app, os.environ.get("SLACK_APP_TOKEN")).start()
