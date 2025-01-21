import requests
import traceback

from _biz.used_cars.utils import get_dict_val_path
from _biz.used_cars.car import Car

cookies = {
    '_ga': 'GA1.1.548999206.1734161694',
    '_cs_c': '0',
    's_ecid': 'MCMID%7C85154234636533927572415030602445466258',
    'ajs_user_id': 'cuida163d65ba53644b3b3fb59d80a1b4942',
    'ajs_anonymous_id': '83d8f22d-f52f-44c0-8165-322350703b29',
    'iterableEndUserId': 'loverszhao%40gmail.com',
    '_gcl_au': '1.1.1024613952.1734325070',
    'vdp': '1',
    '_fbp': 'fb.1.1734325073249.791963372161661331',
    'OptanonAlertBoxClosed': '2024-12-26T22:50:46.507Z',
    'socialLoginProvider': 'google-oauth2',
    'isOneTap': 'true',
    'cfx.auth.logged-in': '1',
    'id': 'google-oauth2%7C102371247105727013854',
    'name': 'loverszhao%40gmail.com',
    'en': 'p',
    'AMCVS_AAC63BC75245B47C0A490D4D%40AdobeOrg': '1',
    's_cc': 'true',
    'abtExperiments': '%5B%5D',
    'QSI_HistorySession': 'https%3A%2F%2Fwww.carfax.com%2Fvehicle%2F3N1AB7AP9KY452642~1736664977571',
    'zip': '94040',
    'payment-calc-info': '%7B%22termInMonths%22%3A%2260%22%2C%22downPaymentPercentage%22%3A10%2C%22interestRate%22%3A%7B%22USED%22%3A7.1%2C%22NEW%22%3A5.4%7D%2C%22creditRange%22%3A%22781%20-%20850%22%7D',
    'crv': '2.604.0',
    'branch-nd': '1',
    'AMCV_AAC63BC75245B47C0A490D4D%40AdobeOrg': '179643557%7CMCIDTS%7C20106%7CMCMID%7C85154234636533927572415030602445466258%7CMCAAMLH-1737789794%7C7%7CMCAAMB-1737789794%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCAID%7CNONE%7CMCOPTOUT-1737192194s%7CNONE%7CvVersion%7C5.5.0',
    'cto_bundle': 'MvbGOl8xMEVUWkQ3OWJpTWh0Nk0yenFPJTJCSW5XeGhUOU1Wb2UwTXFwVlR4elVOUGlxRHlDYWNUMXlwaEpMTG5FRzNsMyUyQk5iMFdRSzA0T01pWW1NRGg0SUVvQWJhYkRQVHlGajlQYXdsbmZodDFGNlRpMHc0N1BQam9BJTJGRlR4M1NIZ0wyUThiVFF6MiUyRm1oSiUyQmJTTVprZ1dxZXEwMElIYW5DTWtXajdCNFNWSGNmblJ3OG80SSUyQjlPaExaemswZ3E1RzM5anMlMkJPOEslMkZYY3ZrQjROR0JsOGp5RnRiZWJJWTg5UWFLVVhqN0Z6Z2w5QnN4MW94dlBKelczMGlia2pCaFR6UkkyTlFyanlLSXpTNXlzZXJuMVpNWE9PV291c0NnbE9XakV4S0xuODFDeUFkRU1TbkZMeDA1SVlGbFRaYVl3dzlTZU0',
    'QSI_SI_0k1Onr1sVkQfZUq_intercept': 'true',
    's_sq': '%5B%5BB%5D%5D',
    '_cs_cvars': '%7B%221%22%3A%5B%22page%20name%22%2C%22Find%20Car%20-%20Details%22%5D%2C%222%22%3A%5B%22site%20section%22%2C%22Find%20a%20Car%22%5D%2C%223%22%3A%5B%22car%20listings%20search%20filters%22%2C%22SO%3ACARFAX%20Best%20Match%7CCO%3AUSED%7CLO%3A94040%7CYR%3A2009-2025%22%5D%2C%224%22%3A%5B%22logged%20in%20status%22%2C%22logged%20in%22%5D%2C%225%22%3A%5B%22partner%20code%22%2C%22DUL_L%22%5D%2C%226%22%3A%5B%22vhr%20permutation%22%2C%22NO_HTL_ICR%22%5D%2C%227%22%3A%5B%22site%20sub%20section%22%2C%22ICR%22%5D%7D',
    'search_uuid': '51c9993c-ce9c-4301-9917-50c8949f064a',
    'ViewContent': '903035815',
    '_cs_id': 'd2969b47-8e6f-a4b2-a58a-a972e79bfd6e.1734161694.51.1737187958.1737184996.1710534941.1768325694033.1',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Sat+Jan+18+2025+00%3A12%3A39+GMT-0800+(Pacific+Standard+Time)&version=202411.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=d1da9b20-cb3a-4907-b190-53d3255af62a&interactionCount=3&isAnonUser=1&landingPath=NotLandingPage&groups=C0002%3A1%2CC0001%3A1%2CC0004%3A1%2CBG135%3A1&AwaitingReconsent=false&intType=1&geolocation=US%3BCA',
    '_ga_KN603HK3Y1': 'GS1.1.1737184994.46.1.1737187959.56.0.0',
    '_uetsid': 'd27501a0d30511efb9e895580c41f1e0',
    '_uetvid': '06612fa0a3c611ef8199ab013359719e',
    'datadome': '_KGFE8RjOkhP00h9XKb2Aatu7BMUwOc9tYG7lPxaD98uVBBY6zM2rbAvhhCkjsKP_RLt26QbQKjAbtJTZKZ8m5c0TJm2cCvD~5F7LYSoUucwcSdnIwIApq45111GaP8_',
}

class CarfaxFetcher():
    def __init__(self, url):
        self.url = url
        self.cars = []
        self.total_pages = 1

    def fetch(self):
        self.fetch_page1()
        for i in range(2, self.total_pages+1):
            self.fetch_pagen(i)

    def get_cars(self):
        blocked_vins = [
            "KMHDH6AH2EU026306",
            "5NPD74LF3HH096032",
            "5NPDH4AE8BH029473",
            "5NPDH4AE7DH410184",
            "5NPDH4AE9EH530778",
            "5NPD84LFXHH149788",
            "5NPD74LF3HH096032"
        ]
        resp = []
        for car in self.cars:
            if car.dealer in ["ADVANTAGE"]:
                continue
            if car.vin in blocked_vins:
                continue
            resp.append(car)
        return resp

    def fetch_page1(self):
        try:
            url = self.url + "1"
            resp = requests.get(url, cookies=cookies)
            print (url)
            print (resp)
            resp_dict = resp.json()
            self.total_pages = get_dict_val_path(resp_dict, "totalPageCount", 1)
            self.enrich_cars(get_dict_val_path(resp_dict, "listings", []))
        except BaseException as e:
            print ("Failed to fetch_page1, e:", e)
            print (traceback.format_exc())

    def fetch_pagen(self, idx):
        try:
            url = self.url + str(idx)
            resp = requests.get(url, cookies=cookies)
            resp_dict = resp.json()
            self.enrich_cars(get_dict_val_path(resp_dict, "listings", []))
        except BaseException as e:
            print ("Failed to fetch_page1, e:", e)
            print (traceback.format_exc())


    def enrich_cars(self, listings):
        print (f"enriching cars count {len(listings)}")
        for listing in listings:
            car = Car(listing)
            self.cars.append(car)



if __name__ == "__main__":
    print ("hi")

    url = "https://helix.carfax.com/search/v2/vehicles?zip=94040&radius=100&sort=BEST&make=Hyundai&model=Elantra&certified=false&vehicleCondition=USED&urlInfo=Hyundai-Elantra_w321&mpgCombinedMin=0&mileageMax=110000&priceMax=11000&dynamicRadius=false&tpPositions=1%2C2%2C3&page="
    fetcher = CarfaxFetcher(url)

    fetcher.fetch()

