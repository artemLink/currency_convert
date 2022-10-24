from django.shortcuts import render
import requests


def main_page(request):
    url = 'https://cdn.cur.su/api/latest.json'
    data = requests.get(url).json()['rates']
    keys = list(data.keys())

    if request.method == 'GET':
        context = {
            'currency': keys
        }
        return render(request, './main/main.html', context=context)

    elif request.method == 'POST':
        amount_from = request.POST.get('convert_from')
        amount_to = request.POST.get('convert_to')
        amount = request.POST.get('amount')
        convert = (data[amount_from] / data[amount_to]) * float(amount)
        context = {
            'currency': keys,
            'convert_amount': convert
        }
        return render(request, './main/main.html', context=context)