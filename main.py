import requests
from bs4 import BeautifulSoup, SoupStrainer
import pyfiglet
import config

class WeatherNotFoundError(Exception):
    pass

BASE_URL = "https://www.google.com/search"
HEADERS = {"user-agent": config.USER_AGENT}

if __name__ == "__main__":
    payload = {"num": 1, "ie": "UTF_8", "q": "weather+"}

    loc_input = input("Enter location: ")
    payload["q"] = payload.get("q", "") + loc_input
    
    try:
        response = requests.get(BASE_URL, params=payload, headers=HEADERS).content
        only_weather = SoupStrainer(id="wob_wc")

        soup = BeautifulSoup(response, "html.parser", parse_only=only_weather)

        f = open("response.txt", "w+")
        f.write(soup.prettify())

        weather = soup.find(id="wob_wc")
        location = soup.find(id="wob_loc")
        date_time = soup.find(id="wob_dts")
        condition = soup.find(id="wob_dc")
        temp_f = soup.find(id="wob_tm")
        temp_c = soup.find(id="wob_ttm")

        if not weather:
            raise WeatherNotFoundError

        print("=====================")
        print(location.text)
        print(date_time.text)
        print(condition.text)
        print("=====================\n")
        print(pyfiglet.figlet_format(temp_f.text + "F" + " " 
            + temp_c.text + "C", font="banner3-D"))

    except requests.exceptions.RequestException as e:
        print(e)

    except WeatherNotFoundError:
        print(f"Unable to find weather for {loc_input}. "
                "Make sure it is a valid location.")
    
    input("Press Enter to exit")