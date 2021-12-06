import emoji

for item in range(6):
    print(item)
print(item)

def funct():
    try:
        return 'from a'
    finally:
        return 'from b'

print(funct())

print(emoji.emojize('Python is amazing:thumbs_up:'))

