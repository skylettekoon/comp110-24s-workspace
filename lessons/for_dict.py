"""Practice with dictionaries and for loops."""

in_stock: dict[str, bool] = {"carrot": True, "beets": False, "apples": True}
# Want to print out true values

for key in in_stock:
    # key is "carrots" "beets" "apples"
    # in_stock[key] is values: True False True
    if in_stock[key] is True:
        print(key)
# Do not need to add "is true", it will check if true by default