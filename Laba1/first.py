from datetime import datetime

name = "Роман"
activity = "програмувати"

current_time = datetime.now().strftime("%d.%m.%Y %H:%M:%S")

print(f"{name} почав {activity} о {current_time}.")
