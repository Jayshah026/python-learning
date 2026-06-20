letter = '''Hello <|Name|>
You have been selected 
Come to office on <|Date|>'''

print(letter.replace("<|Name|>", "Jay").replace("<|Date|>", "10-06-26"))