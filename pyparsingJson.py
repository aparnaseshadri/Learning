In Python, you can access JSON data using the built-in `json` module, which allows you to parse JSON strings into Python objects and vice versa.

### **Common Tasks:**
1. **Parse JSON from a string or file into Python objects.**
2. **Access and manipulate the data like dictionaries or lists.**

---

### **Example 1: Parse JSON from a String**

```python
import json

# JSON data as a string
json_data = '{"name": "Aparna", "age": 30, "skills": ["Python", "Kubernetes"]}'

# Parse the JSON string into a Python dictionary
data = json.loads(json_data)

# Access the data
print(data["name"])        # Output: Aparna
print(data["age"])         # Output: 30
print(data["skills"][0])   # Output: Python
```

### **Example 2: Parse JSON from a File**

```python
import json

# Read JSON data from a file
with open('data.json', 'r') as file:
    data = json.load(file)

# Access the data
print(data["name"])
print(data["skills"])
```

### **Example 3: Convert Python Object to JSON String**

```python
import json

# Python dictionary
python_data = {
    "name": "Aparna",
    "age": 30,
    "skills": ["Python", "Kubernetes"]
}

# Convert to JSON string
json_string = json.dumps(python_data, indent=2)
print(json_string)
```

### **Explanation of Key Methods:**
1. **`json.loads()`**: Parses a JSON string into a Python object (dict).
2. **`json.load()`**: Parses JSON data from a file.
3. **`json.dumps()`**: Converts a Python object to a JSON string.
4. **`json.dump()`**: Writes a Python object to a file in JSON format.

---

### Summary:
- Use `json.loads()` for JSON strings and `json.load()` for JSON files.
- Access JSON data in Python as you would with dictionaries or lists.
- Use `json.dumps()` to serialize Python objects back to JSON strings.
