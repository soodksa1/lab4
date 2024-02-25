from django.shortcuts import render

tax_rate = 0.15

def Default_path(request):
    return render(request, 'taxes/Default_path.html')

def calculate_tax(request, price):
    
        price = float(price)
        total_price = price * tax_rate
        context = {'price': price, 'total_price': total_price}
        return render(request, 'taxes/calculate_tax.html', context)

def show_tax_rate(request):
    context = {'tax_rate': tax_rate}
    return render(request, 'taxes/tax_rate.html', context)   

