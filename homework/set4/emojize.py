
input = input("Input: ")

emojis = {
    ":1st_place_medal:":"🥇",
    ":money_bag:":"💰",
    ":smile_cat:":"😸",
    ":thumbs_up:":"👍",
	":earth_americas:":"🌎",
    ":globe_showing_americas:":"🌎",
    ":earth_asia:":"🌏",
    ":globe_showing_asia_australia:":"🌏",
    ":earth_africa:":"🌍",
    ":globe_showing_europe_africa:":"🌍"
}

for word,emoji in emojis.items():
    if word in input:
        print(input)
        input = input.replace(word, emoji)
    else:
        new_word = word.replace("_", "")
        if new_word in input:
            input = input.replace(new_word, emoji)

print(input)