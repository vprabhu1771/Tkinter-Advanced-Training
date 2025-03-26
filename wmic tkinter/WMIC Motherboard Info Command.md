You can use Python's `re` module to process the output and extract the motherboard details in a structured format. Here’s how you can do it:

### Python Script:
```python
import subprocess
import re

def get_motherboard_info():
    command = "wmic baseboard get Manufacturer, Product, SerialNumber, Version"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    
    if result.returncode == 0:
        output = result.stdout.strip()
        
        # Using regex to extract the Manufacturer, Product, SerialNumber, and Version
        match = re.search(r"(\S.*\S)\s+(\S.*\S)\s+(\S+)\s+(\S.*\S)", output.split("\n", 1)[1])
        
        if match:
            motherboard_info = {
                "Manufacturer": match.group(1).strip(),
                "Product": match.group(2).strip(),
                "SerialNumber": match.group(3).strip(),
                "Version": match.group(4).strip()
            }
            return motherboard_info
        else:
            return "Error parsing motherboard information"
    else:
        return "Error retrieving motherboard information"

if __name__ == "__main__":
    info = get_motherboard_info()
    print(info)
    print(info['Manufacturer'])
    print(info['Product'])
    print(info['SerialNumber'])
    print(info['Version'])
```

### Explanation:
1. Executes `wmic baseboard get Manufacturer, Product, SerialNumber, Version`.
2. Uses `re.search()` to extract values:
   - `(\S.*\S)`: Captures the Manufacturer.
   - `(\S.*\S)`: Captures the Product.
   - `(\S+)`: Captures the SerialNumber.
   - `(\S.*\S)`: Captures the Version.
3. Returns a dictionary with the parsed details.

### Sample Output:
```python
{
    'Manufacturer': 'ASUSTeK COMPUTER INC.',
    'Product': 'TUF GAMING Z590-PLUS',
    'SerialNumber': '1234567890',
    'Version': 'Rev 1.xx'
}
```

This ensures you extract motherboard details accurately. Let me know if you need improvements! 🚀
