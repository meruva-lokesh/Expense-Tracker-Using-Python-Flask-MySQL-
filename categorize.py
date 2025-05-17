def categorize_receipt(items):
    categories = {
        'food': ['burger', 'pizza', 'restaurant', 'sandwich', 'cafe', 'food', 'meal'],
        'grocery': ['walmart', 'grocery', 'vegetable', 'fruit', 'milk', 'supermarket'],
        'transport': ['uber', 'lyft', 'taxi', 'bus', 'train', 'transport'],
        'shopping': ['amazon', 'clothes', 'shoes', 'shopping', 'mall'],
        'other': []
    }
    result = []
    for item in items:
        assigned = False
        for cat, keywords in categories.items():
            if any(word in item.lower() for word in keywords):
                result.append({'item': item, 'category': cat})
                assigned = True
                break
        if not assigned:
            result.append({'item': item, 'category': 'other'})
    return result