#!/usr/bin/env python

from flask import Flask, render_template

from _biz.used_cars.carfax_fetcher import CarfaxFetcher

app = Flask(__name__)


def run(url):
    fetcher = CarfaxFetcher(url)
    fetcher.fetch()
    cars = fetcher.get_cars()
    print (f"cars count {len(cars)}")

    # 渲染 index.html，传入一些变量
    return render_template('index.html', title="Flask 测试", name="Alice", cars=cars)


@app.route('/')
def home():
    url = "https://helix.carfax.com/search/v2/vehicles?zip=94040&yearMin=2010&radius=200&sort=BEST&make=Hyundai&model=Elantra&certified=false&vehicleCondition=USED&urlInfo=Hyundai-Elantra_w321&mpgCombinedMin=0&mileageMax=110000&priceMax=11000&dynamicRadius=false&tpPositions=1%2C2%2C3&page="
    return run(url)


@app.route('/los')
def los():
    url = "https://helix.carfax.com/search/v2/vehicles?zip=90019&yearMin=2010&radius=200&sort=BEST&make=Hyundai&model=Elantra&certified=false&vehicleCondition=USED&urlInfo=Hyundai-Elantra_w321&mpgCombinedMin=0&mileageMax=110000&priceMax=11000&dynamicRadius=false&tpPositions=1%2C2%2C3&page="
    return run(url)


if __name__ == '__main__':
    app.run(debug=True)
