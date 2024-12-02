calls = 0
def count_calls ():
    global calls
    calls += 1
def string_info (string):
    count_calls()
    return (len(string), string.upper(), string.lower())
def is_contains (string, list_to_search):
    count_calls()
    return string.upper() in [a.upper() for a in list_to_search]

print(string_info('Defender'))
print(string_info('description'))
print(is_contains('Takedown',['down','TaKeDoWn','takeDOWN']))
print(is_contains('style',['styling','flair']))
print(calls)

