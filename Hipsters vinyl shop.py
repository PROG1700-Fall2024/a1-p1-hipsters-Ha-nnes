
"""
Student Name: Hannes Meyer-Rahlfs   
Program Title: Hipster's Local Vinyl Records   
"""
  # Constants
Delivery_Rate_Per_KM = 15.0  # $15per kilometer
Sales_Tax_Rate = 0.14  # 14% sales tax

# Input customer information
customer_name = input("Enter the customer's name: ")
distance_in_km = float(input("Enter the distance in kilometers: "))
records_cost = float(input("Enter the cost of records purchased: "))

# Calculate delivery cost
delivery_cost = distance_in_km * Delivery_Rate_Per_KM

# Calculate records cost with tax
records_cost_with_tax = records_cost + (records_cost * Sales_Tax_Rate)

# Calculate total cost
total_cost = delivery_cost + records_cost_with_tax

# Output the results
print("Customer Name: " + customer_name)
print(f"Delivery Cost: ${delivery_cost:.2f}")
print(f"Purchase Cost (with tax): ${records_cost_with_tax:.2f}")
print(f"Total Cost: ${total_cost:.2f}")

 # Ready for Marking
