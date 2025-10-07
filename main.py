from pyscript import document

def create_order(e):
    name = document.getElementById("name").value.strip()
    haus = document.getElementById("address").value.strip()
    contact = document.getElementById("contact").value.strip()

    if not name or not haus or not contact:
        document.getElementById("orderSummary").innerText = "Fill in all the details."
        return 

    items = [
        {"id": "sisig", "name": "Pork Sisig", "price": 180},
        {"id": "bulalo", "name": "Bulalo", "price": 240},
        {"id": "sinigang", "name": "Pork Sinigang", "price": 230},
        {"id": "manok", "name": "Lechon Manok", "price": 190},
        {"id": "tea", "name": "Iced Tea", "price": 90},
        {"id": "coke", "name": "Coca-Cola", "price": 100},
        {"id": "sprite", "name": "Sprite", "price": 100},
        {"id": "mango", "name": "Mango Juice", "price": 140}
    ]

    total = 0
    selected_items = []

    for item in items:
        checkbox = document.getElementById(item["id"])
        if checkbox.checked:
            total += item["price"]
            selected_items.append(item["name"])

    if not selected_items:
        document.getElementById("orderSummary").innerText = "Select at least one item."
        return
    
    summary = f"""
        Order for: {name}
        Address: {haus}
        Contact: {contact}

        Items ordered:
        """
    
    for item in selected_items:
        summary += f"- {item}\n"

    summary += f"\nTotal: ₱{total}"

    document.getElementById("orderSummary").innerText = summary
