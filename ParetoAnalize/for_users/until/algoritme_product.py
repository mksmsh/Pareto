from for_users.models import Shop, Product, Sale
from django.db.models import Sum


def SaleAnalizeProduct(shop):

    sales = Sale.objects.filter(shop=shop)

    aggregated_data = {}

    for sale in sales:
        name = sale.name_p
        if name not in aggregated_data:
            aggregated_data[name] = {
                'sum_d': 0,
                'sum_p': 0,
            }

        aggregated_data[name]['sum_d'] += sale.price * sale.count
        aggregated_data[name]['sum_p'] += sale.profit * sale.count


    data_array = []

    for name, values in aggregated_data.items():
        sum_d = round(values['sum_d'],0)
        sum_p = round(values['sum_p'], 0)

        profitability = round((sum_p / sum_d) * 100 if sum_d != 0 else 0, 1)

        data_array.append({
            'name': name,
            'sum_d': sum_d,
            'sum_p': sum_p,
            'profitability': profitability,
        })

    total_sum_d_from_array = sum(item['sum_d'] for item in data_array)
    total_sum_p_from_array = sum(item['sum_p'] for item in data_array)

    new_data_array = []

    all_procent_price = 0
    all_procent_profit = 0

    sorted_data_array = sorted(data_array, key=lambda x: x['profitability'], reverse=True)

    for item in sorted_data_array:
        group_procent_price = round((item['sum_d'] / total_sum_d_from_array) * 100, 1)
        all_procent_price = all_procent_price + group_procent_price
        group_procent_profit = round((item['sum_p'] / total_sum_p_from_array) * 100, 1)
        all_procent_profit= all_procent_profit + group_procent_profit

        new_data_array.append({
            'name': item['name'],
            'sum_d': item['sum_d'],
            'sum_p': item['sum_p'],
            'profitability': item['profitability'],
            'group_procent_price': group_procent_price,
            'group_procent_profit': group_procent_profit,
            'all_procent_price': all_procent_price,
            'all_procent_profit': all_procent_profit
        })

    return new_data_array, total_sum_d_from_array, total_sum_p_from_array


def ProductAnalizeProduct(shop):

    products = Product.objects.filter(shop=shop)

    aggregated_data = {}

    for product in products:
        name = product.nameP
        if name not in aggregated_data:
            aggregated_data[name] = {
                'sum_d': 0,
                'sum_p': 0,
            }

        if product.price is not None:
            aggregated_data[name]['sum_d'] += product.price

        aggregated_data[name]['sum_p'] += product.profit


    data_array = []

    for name, values in aggregated_data.items():
        sum_d = round(values['sum_d'],0)
        sum_p = round(values['sum_p'], 0)

        profitability = round((sum_p / sum_d) * 100 if sum_d != 0 else 0, 1)

        data_array.append({
            'name': name,
            'sum_d': sum_d,
            'sum_p': sum_p,
            'profitability': profitability,
        })

    total_sum_d_from_array = sum(item['sum_d'] for item in data_array)
    total_sum_p_from_array = sum(item['sum_p'] for item in data_array)

    new_data_array = []

    all_procent_price = 0
    all_procent_profit = 0

    sorted_data_array = sorted(data_array, key=lambda x: x['profitability'], reverse=True)

    for item in sorted_data_array:
        group_procent_price = round((item['sum_d'] / total_sum_d_from_array) * 100, 1)
        all_procent_price = all_procent_price + group_procent_price
        group_procent_profit = round((item['sum_p'] / total_sum_p_from_array) * 100, 1)
        all_procent_profit= all_procent_profit + group_procent_profit

        new_data_array.append({
            'name': item['name'],
            'sum_d': item['sum_d'],
            'sum_p': item['sum_p'],
            'profitability': item['profitability'],
            'group_procent_price': group_procent_price,
            'group_procent_profit': group_procent_profit,
            'all_procent_price': all_procent_price,
            'all_procent_profit': all_procent_profit
        })

    return new_data_array, total_sum_d_from_array, total_sum_p_from_array