from django.http import HttpResponse
from django.shortcuts import render

tax_rate = 0.15  # Tax rate variable

def home(request):
    # Default view
    return HttpResponse('This is a site to calculate tax.')

def calculate_tax(request, price):
    # Calculates total price including tax
    total_price = price + (price * tax_rate)
    return HttpResponse(f'Total price with tax: {total_price}')

def taxrate(request):
    # Displays the tax rate
    return render(request, 'tax_rate.html', {'tax_rate': tax_rate * 100})
