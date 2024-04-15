import os


SS = "WORKERS_DATA"
if "WORKERS_DATA" in os.environ:
    print(f"Переменная окружения {SS} установлена.")
else:
    print("Переменная окружения WORKERS_DATA не установлена.")
