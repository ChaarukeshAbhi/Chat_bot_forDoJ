import json
import re

# Load the unstructured data from the JSON file
with open('unstructured_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Initialize a list to store cleaned data
cleaned_data = []

for entry in data:
    # Clean content
    content = entry.get('content', '')
    content = content.strip()  # Remove leading/trailing whitespace
    content = re.sub(r'\s+', ' ', content)  # Replace multiple spaces/newlines with a single space
    content = re.sub(r'<.*?>', '', content)  # Remove any HTML tags
    content = content.lower()  # Convert to lowercase

    # Update the entry with cleaned content
    entry['content'] = content

    # Filter out empty or irrelevant entries
    if content:  # Keep only non-empty content
        cleaned_data.append(entry)

# Optional: Remove special characters/punctuation (depends on your needs)
for entry in cleaned_data:
    entry['content'] = re.sub(r'[^\w\s]', '', entry['content'])

# Save the cleaned data back to a new JSON file
output_file = 'cleaned_data.json'
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(cleaned_data, f, ensure_ascii=False, indent=4)

print(f"Cleaned data saved to {output_file}")
