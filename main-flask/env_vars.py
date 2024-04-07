import os
from dotenv import load_dotenv

load_dotenv()

AMQP_URL = str(os.environ['AMQP_URL'])
