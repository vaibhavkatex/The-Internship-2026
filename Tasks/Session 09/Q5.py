# Q5. (update() and pop())
# Create a dictionary: info = {"brand": "Samsung", "model": "A52", "price": 25000}
# Update it with new information: {"color": "Black", "price": 24000}.
# Remove the key "model" using pop() and print the removed value.
# Print the final dictionary.


# Q5. (update() and pop())

info = {
    "brand": "Samsung",
    "model": "A52",
    "price": 25000
}

# Update dictionary
info.update({
    "color": "Black",
    "price": 24000
})

# Remove "model" and store removed value
rm_value = info.pop("model")

# Print removed value
print("Removed Value:", rm_value)

# Print final dictionary
print("Final Dictionary:", info)