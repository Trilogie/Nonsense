favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

friends = ['phil', 'sarah']

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite language are:")
    for language in languages:
        print(f"\t{language.title()}")

