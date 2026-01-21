placeholder_mapping = {
    "{{customer_name}}": "Customer Name",
    "{{product_id}}": "Product ID",
    "{{date}}": "Order Date"
}

def load_mapping():
    return {
        "{{customer_name}}": "Customer Name",
        "{{product_id}}": "Product ID",
        "{{date}}": "Order Date"
    }

mapping = load_mapping()

def get_column_header(placeholder, mapping):
    if placeholder not in mapping:
        raise KeyError(f"No mapping found for {placeholder}")
    return mapping[placeholder]

print(get_column_header("{{customer_name}}", mapping))
print(get_column_header("{{product_id}}", mapping))
print(get_column_header("{{date}}", mapping))
