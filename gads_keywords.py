# Bulk generate phrase match and exact match keywords

# paste raw keywords below
keyword_text = """
"""

# Process the keywords
keywords = [line.strip() for line in keyword_text.strip().split('\n') if line.strip()]

# Format and output
print("broad match:")
for keyword in keywords:
    print(f"[{keyword}]")

print("\nphrase match:")
for keyword in keywords:
    print(f'"{keyword}"')
