Sure! Here is a sample Python code that uses the `requests` library to achieve the same functionality as a curl command:

```python
import requests

url = "https://www.example.com"
response = requests.get(url)

if response.status_code == 200:
    data = response.text
    print(data)
else:
    print("Failed to retrieve data. Status code:", response.status_code)
```

This code sends a GET request to the specified URL using the `requests.get()` method and then prints the response data if the status code is 200 (OK). You can modify the `url` variable to fetch data from a different website.