import os
import pandas as pd
import numpy as np
from datetime import datetime

os.system('cls')

dt = "13/05/2011"

dto = datetime.strptime(dt, '%d/%m/%Y').date()

print(dto)