Sure! Here is a sample Python code that creates a function to convert CSV files to JSON format:

```python
import csv
import json

def convert_csv_to_json(csv_file_path, json_file_path):
    data = []
    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(row)

    with open(json_file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)

# Usage example
convert_csv_to_json('input.csv', 'output.json')
```

In this code snippet, the `convert_csv_to_json` function takes the file paths of the input CSV file and the output JSON file as parameters. It reads the data from the CSV file, converts it into a list of dictionaries, and then writes the data to the JSON file using the `json.dump` method.