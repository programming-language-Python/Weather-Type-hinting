from pathlib import Path

from coordinates import get_gps_coordinates
from exceptions import ApiServiceError
from exceptions import CantGetCoordinates
from history import PlainFileWeatherStorage
from history import JSONFileWeatherStorage
from history import save_weather
from weather_api_service import get_weather
from weather_formatter import format_weather


def main():
    try:
        coordinates = get_gps_coordinates()
        print(f"Широта:", coordinates.latitude)  # Печать широты
        print(f"Долгота:", coordinates.longitudeRRR)  # IDE подсветит ошибку опечатки
    except CantGetCoordinates:
        print("Не смог получить GPS-координаты")
        exit(1)
    try:
        weather = get_weather(coordinates)
    except ApiServiceError:
        print("Не смог получить погоду в API-сервиса погоды")
        exit(1)
    save_weather(
        weather,
        PlainFileWeatherStorage(Path.cwd() / "history.txt")
    )
    save_weather(
        weather,
        JSONFileWeatherStorage(Path.cwd() / "history.json")
    )
    print(format_weather(weather))


if __name__ == "__main__":
    main()
