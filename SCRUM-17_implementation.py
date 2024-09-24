Certainly! Below is an example of Python code that creates a simple earnings functionality dashboard for a chatbot using the `matplotlib` library:

```python
import matplotlib.pyplot as plt

# Sample earnings data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
earnings = [1000, 1200, 800, 1500, 1300]

# Create a bar chart to visualize earnings data
plt.figure(figsize=(8, 6))
plt.bar(months, earnings, color='skyblue')
plt.xlabel('Months')
plt.ylabel('Earnings ($)')
plt.title('Earnings Dashboard')
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.show()
```

This code snippet uses `matplotlib` to create a bar chart representing earnings data for different months. You can customize the code further based on your specific requirements and data structure.