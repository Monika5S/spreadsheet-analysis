import csv
import matplotlib.pyplot as plt

def getMonthlySales(sales_data):
    sales_by_month = {}

    for row in sales_data:
        month=row['month']
        sale=int(row['sales'])
        if month in sales_by_month:
            sales_by_month[month]+=sale
        else:
            sales_by_month[month]=sale

    print('Sales by month: {}'.format(sales_by_month))
    return sales_by_month

def getSalesData():
    with open('sales.csv', 'r') as sales:
        #collecting sales from each month into a single list
        sales_data=list(csv.DictReader(sales))
    return sales_data

def main():
    #Reading the data from the spreadsheet
    sales_data=getSalesData()

    #total sales across all months
    total_sales=0
    for row in sales_data:
        total_sales+=int(row['sales'])
    print('Total sales: {}'.format(total_sales))

    #finding monthly sales
    sales_by_month=getMonthlySales(sales_data)

    #finding month with the highest sales
    highest_sale=0
    highest_sale_month=''
    for month, sale in sales_by_month.items():
        if sale>highest_sale:
            highest_sale=sale
            highest_sale_month=month
    print('Highest sales: {} in {}'.format(highest_sale, highest_sale_month))

    #finding month with the lowest sales
    lowest_sale=highest_sale
    lowest_sale_month=''
    for month, sale in sales_by_month.items():
        if sale<lowest_sale:
            lowest_sale=sale
            lowest_sale_month=month
    print('Lowest sales: {} in {}'.format(lowest_sale, lowest_sale_month))
   
    #line graph showing highest and lowest sales
    months=[]
    sales=[]
    for month, sale in sales_by_month.items():
        months.append(month)
        sales.append(sale)

    plt.plot(months, sales)
    plt.title('Monthly sales')
    plt.xlabel('Month')
    plt.ylabel('Sales')

    plt.plot(highest_sale_month, highest_sale, 'ro')
    plt.plot(lowest_sale_month, lowest_sale, 'ro')
    plt.text(highest_sale_month, highest_sale, 'Highest sale')
    plt.text(lowest_sale_month, lowest_sale, 'Lowest sale')
    plt.show()

main()