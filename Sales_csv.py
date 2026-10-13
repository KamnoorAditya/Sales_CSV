import csv

total_revenue = 0
region_revenue = {}
product_revenue = {}

with open("sales.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        region = row["region"]
        product = row["product"]
        amount = float(row["amount"])

        total_revenue += amount

        if region not in region_revenue:
            region_revenue[region] = 0

        region_revenue[region] += amount

        if product not in product_revenue:
            product_revenue[product] = 0

        product_revenue[product] += amount

print(f"Total Revenue: {total_revenue}")

print("\nRevenue Per Region:")
for region, revenue in region_revenue.items():
    print(f"{region}: {revenue}")

def get_revenue(item):
    return item[1]

sorted_products = sorted(
    product_revenue.items(),
    key=get_revenue,
    reverse=True
)

print("\nTop 3 Products by Revenue:")
for product, revenue in sorted_products[:3]:
    print(f"{product}: {revenue}")
