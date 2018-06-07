from YoulaAdmin.controller.client import Client
from YoulaAdmin.controller.environment import Environment

environment = Environment(
    protocol="https",
    host="api.youla.devmail.ru",
    path="admin"
)

admin_cli = Client(
   
)


u = admin_cli.test_action_push_message.send_to_user(
    user_id="5a5c6d355f903748261d9b43",
    text="Test",
    type=11,
    screen=3
)