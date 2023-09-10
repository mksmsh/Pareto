from for_users.models import Shop, Product, Sale
from django.db.models import Sum


def SaleAnalizeProduct(shop):
    data_array = []
    sales = Sale.objects.filter(shop=shop)

    aggregated_data = sales.values('name_p').annotate(
        sum_d=Sum(Sale.price * Sale.count),
        sum_p=Sum(Sale.profit * Sale.count)
    )

    for item in aggregated_data:
        sum_d = item['sum_d']
        sum_p = item['sum_p']

        profitability = (sum_p / sum_d) * 100 if sum_d != 0 else 0

        data_array.append({
            'name_p': item['name_p'],
            'sum_d': sum_d,
            'sum_p': sum_p,
            'profitability': profitability
        })


    total_sum_d_from_array = sum(item['sum_d'] for item in data_array)
    total_sum_p_from_array = sum(item['sum_p'] for item in data_array)

    new_data_array = []

    all_procent_price = 0
    all_procent_profit = 0

    for item in data_array:
        group_procent_price = (item['sum_d'] / total_sum_d_from_array) * 100
        group_procent_profit = (item['sum_p'] / total_sum_p_from_array) * 100

        all_procent_price += group_procent_price
        all_procent_profit += group_procent_profit

        new_data_array.append({
            'name_p': item['name_p'],
            'group_procent_price': group_procent_price,
            'group_procent_profit': group_procent_profit,
            'all_procent_price': all_procent_price,
            'all_procent_profit': all_procent_profit
        })

    return new_data_array

def ProductAnalizeProduct(shop):
    data_array = []
    products = Product.objects.filter(shop=shop)

    for product in products:
        price = product['price']
        profit = product['profit']

        profitability = (profit / price) * 100 if price != 0 else 0

        data_array.append({
            'nameP': products['nameP'],
            'price': price,
            'profit': profit,
            'profitability': profitability
        })


    total_sum_d_from_array = sum(product['price'] for product in data_array)
    total_sum_p_from_array = sum(product['profit'] for product in data_array)

    new_data_array = []

    all_procent_price = 0
    all_procent_profit = 0

    for product in data_array:
        group_procent_price = (product['price'] / total_sum_d_from_array) * 100
        group_procent_profit = (product['profit'] / total_sum_p_from_array) * 100

        all_procent_price += group_procent_price
        all_procent_profit += group_procent_profit

        new_data_array.append({
            'nameP': product['nameP'],
            'group_procent_price': group_procent_price,
            'group_procent_profit': group_procent_profit,
            'all_procent_price': all_procent_price,
            'all_procent_profit': all_procent_profit
        })

    return new_data_array