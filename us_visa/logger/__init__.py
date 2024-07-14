import logging
import os 

from from_root import from_root
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_&H_%M_%S')}.log"

log_dir = 'logs'

log_path = os.path(from_root(), LOG_FILE)

os.mkdirs(log_dir, exist_ok=True)

logging.basicConfig(
    filename=log_path,
    format="[%(asctime)s] %(name)s -%(levelname)s %(message)s",
    level=logging.DEBUG
)