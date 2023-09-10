from for_users.models import Shop, Product, Sale
from django.db.models import Sum


def SaleAnalizeCategory(shop):
    data_array = []
    sales = Sale.objects.filter(shop=shop)

    aggregated_data = {}

    for sale in sales:
        category = sale.category
        if category not in aggregated_data:
            aggregated_data[category] = {
                'sum_d': 0,
                'sum_p': 0,
            }

        aggregated_data[category]['sum_d'] += sale.price * sale.count
        aggregated_data[category]['sum_p'] += sale.profit * sale.count

    # Преобразование словаря в список, если это необходимо
    data_array = []
    for category, values in aggregated_data.items():
        sum_d = values['sum_d']
        sum_p = values['sum_p']

        profitability = (sum_p / sum_d) * 100 if sum_d != 0 else 0

        data_array.append({
            'category': category,
            'sum_d': sum_d,
            'sum_p': sum_p,
            'profitability': profitability,  # Добавляем рентабельность к элементу
        })

    total_sum_d_from_array = sum(item['sum_d'] for item in data_array)
    total_sum_p_from_array = sum(item['sum_p'] for item in data_array)

    new_data_array = []

    all_procent_price = 0
    all_procent_profit = 0

    sorted_data_array = sorted(data_array, key=lambda x: x['profitability'], reverse=True)

    for item in sorted_data_array:
        group_procent_price = (item['sum_d'] / total_sum_d_from_array) * 100
        all_procent_price=+ group_procent_price
        group_procent_profit = (item['sum_p'] / total_sum_p_from_array) * 100
        all_procent_profit=+ all_procent_profit

        new_data_array.append({
            'category': item['category'],
            'group_procent_price': group_procent_price,
            'group_procent_profit': group_procent_profit,
            'all_procent_price': all_procent_price,
            'all_procent_profit': all_procent_profit
        })

    return new_data_array


def ProductAnalizeCategory(shop):

    data_array = []
    products = Product.objects.filter(shop=shop)

    aggregated_data = products.values('category').annotate(
        sum_d=Sum(products.price),
        sum_p=Sum(products.profit)
    )

    for product in aggregated_data:
        sum_d = product['sum_d']
        sum_p = product['sum_p']

        profitability = (sum_p / sum_d) * 100 if sum_d != 0 else 0

        data_array.append({
            'category': product['category'],
            'sum_d': sum_d,
            'sum_p': sum_p,
            'profitability': profitability
        })


    total_sum_d_from_array = sum(products['sum_d'] for products in data_array)
    total_sum_p_from_array = sum(products['sum_p'] for products in data_array)

    new_data_array = []

    all_procent_price = 0
    all_procent_profit = 0

    for product in data_array:
        group_procent_price = (product['sum_d'] / total_sum_d_from_array) * 100
        group_procent_profit = (product['sum_p'] / total_sum_p_from_array) * 100

        all_procent_price += group_procent_price
        all_procent_profit += group_procent_profit

        new_data_array.append({
            'category': product['category'],
            'group_procent_price': group_procent_price,
            'group_procent_profit': group_procent_profit,
            'all_procent_price': all_procent_price,
            'all_procent_profit': all_procent_profit
        })


    return new_data_array