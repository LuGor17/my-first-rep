# sales_data.py
# Weekly sales data: [Ponedjeljak, Utorak, Srijeda, Četvrtak, Petak, S, Sunday]
sales_data = [230, 200, 310, 290, 400, 150, 180]

def total_sales(data):
    return sum(data)

def average_sales(data):
    return sum(data) / len(data)

# Pozivanje funkcija i prikaz rezultata
print(f"Total sales: {total_sales(sales_data)}")
print(f"Average sales: {average_sales(sales_data):.2f}")