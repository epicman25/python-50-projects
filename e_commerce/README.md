# Simple E-commerce Store

**Difficulty Level:** Intermediate (Est. 2-3 Hours)

## Project Description
Model a simple e-commerce system. Create a `Product` class (name, price, quantity_in_stock) and a `ShoppingCart` class. The `ShoppingCart` class should have methods like `add_item(product, quantity)`, `remove_item(product)`, and `calculate_total()`. This project focuses on class composition (a ShoppingCart "has" Products).

## Possible Folder Structure
```
e_commerce/
├── main.py        # (Simulates adding items to a cart)
├── product.py     # (Contains Product class)
└── shopping_cart.py # (Contains ShoppingCart class)
```

## Inputs and Expected Outputs
- **Input:** (In main.py) `cart.add_item(product_A, 2)`, `cart.add_item(product_B, 1)`
- **Output:** `print(cart.calculate_total())` -> `55.97`

## Learning Objectives
- Class composition
- E-commerce logic
- Object relationships
- Shopping cart functionality
