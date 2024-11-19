
import requests
from decimal import Decimal
from django.shortcuts import render


def index(request):
    # Your API URL for Speed balance
    url = "https://api.tryspeed.com/balances"
    headers = {
        "accept": "application/json",
        "authorization": "Basic cmtfbGl2ZV9seWs0bzY5cDd2Ym5UWlU0bHplMGs0bHdGUDV0NVEzcmx6ZTBrNGx3eXpNelprQVQ6VGhlVmlsbGFnZUh1YjE="
    }
    response = requests.get(url, headers=headers)
    response_data = response.json()
    speed_balance = response_data["available"][0]["amount"]

    # Convert to BTC
    btc_amount = Decimal(speed_balance) / Decimal(100000000)

    # Get form data satsinput
    if request.method == 'POST':
        satsinput = request.POST.get('satsinput')
        btc_amount2 = float(satsinput)
        btc_amount2 = Decimal(btc_amount2) / Decimal(100000000)
        btc_amount3 = int(btc_amount2*100000000)

    else:
        btc_amount2 = 0
        btc_amount3 = 0


    # Get ZAR price
    zar_price = get_bitcoin_price()

    # Calculate ZAR value
    zar_value = btc_amount * zar_price
    zar_value2 = btc_amount2 * zar_price
    zar_value3 = zar_price
    
    context = {'zar_value': zar_value, 'zar_value2': zar_value2, 'zar_value3': zar_value3, 'btc_amount3': btc_amount3, 'speed_balance': int(speed_balance),}
    return render(request, 'sats/index.html', context)

def get_bitcoin_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=zar"
    response = requests.get(url)
    data = response.json()
    return Decimal(data.get("bitcoin", {}).get("zar", 0))



