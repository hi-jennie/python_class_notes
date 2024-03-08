answer = input(
    "What is the Answer to the Great Question of life, the Universe, and Everthing?"
).strip()

answer = answer.upper()
match answer:
    case "42":
        print("Yes")
    case "FORTY-TWO" | "FORTY TWO":
        print("Yes")
    case _:
        print("No")
