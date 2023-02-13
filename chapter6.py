alien_0 = {"color": "yellow", "point": "5"}
print(alien_0["color"])
print(alien_0["point"])

alien_0["x_position"] = 0
alien_0["y_position"] = 10

# print(alien_0)


favorite_language = {
    "kobe": "python",
    "tmac": "java",
    "tom": "python",
    "lily": "python",
}
print(favorite_language)

del favorite_language["kobe"]
print(favorite_language)

print("\n")
for k, v in favorite_language.items():
    print(f"key is {k},value is {v}")

# 用字典的.keys方法返回字典中的键列表
print("\n")
for name in favorite_language.keys():
    print(name)


# 默认循环字典中的键
print("\n")
for name in favorite_language:
    print(name)

# 判断当前是否在字典的键列表中
print("\n")
if "james" not in favorite_language.keys():
    print("james not in the list")


# 按顺序返回字典中的键
print("\n")
for name in sorted(favorite_language.keys()):
    print(name)


print("\n")
for language in favorite_language.values():
    print(language)


# 去重，拿出字典中的值列表
print("\n")
for language in set(favorite_language.values()):
    print(language)
