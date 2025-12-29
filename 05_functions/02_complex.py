def fetch_sales():
    print("Fetching sales data...")


def filter_valid_sales(sales):
    print("Filtering valid orders...")


def summarize_data(sales):
    print("Summarizing sales...")


def generate_report():
    sales = fetch_sales()
    valid_sales = filter_valid_sales(sales)
    summarized_data = summarize_data(valid_sales)
    return summarized_data


report = generate_report()
print(report)
