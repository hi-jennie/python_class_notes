#{fruit_calory[item]}" ,使用变量item作为key去取他对应的value时，不打“”


item = input("Item: ").lower()

fruit_calory = {
    "apple":"130",
    "avocado":"50",
    "sweet cherries":"100",
    "kiwifruit":"90",
    "pear":"100"
}

if item in fruit_calory:
    print(f"Calories: {fruit_calory[item]}")

pass
