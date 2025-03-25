You can list the available attributes and methods of the `winreg` module in Python using the `dir()` function. Here's how you do it:

```python
import winreg

print(dir(winreg))
```

This will return a list of all functions, constants, and classes available in the `winreg` module.

Would you like me to explain specific functions from the `winreg` module?


The `winreg` module in Python provides an interface for interacting with the Windows Registry. Below is an explanation of some key functions and constants available in `winreg`:

### **Main Functions**
1. **`winreg.ConnectRegistry(computer_name, key)`**  
   - Connects to a remote or local registry.
   - `computer_name`: Use `None` for local or specify a remote computer name.
   - `key`: A predefined root key (e.g., `HKEY_LOCAL_MACHINE`).
   - Returns a handle to the connected registry.

2. **`winreg.OpenKey(key, sub_key, reserved=0, access=KEY_READ)`**  
   - Opens a registry key.
   - `key`: A handle to an already open key or a predefined root key.
   - `sub_key`: The path of the subkey to open.
   - `reserved`: Must be `0`.
   - `access`: Access rights (`KEY_READ`, `KEY_WRITE`, etc.).
   - Returns a handle to the opened key.

3. **`winreg.CreateKey(key, sub_key)`**  
   - Creates a new registry key or opens it if it exists.
   - Returns a handle to the key.

4. **`winreg.DeleteKey(key, sub_key)`**  
   - Deletes a specified key if it has no subkeys.

5. **`winreg.DeleteValue(key, value_name)`**  
   - Deletes a specified value from a registry key.

6. **`winreg.QueryValueEx(key, value_name)`**  
   - Retrieves the data and type of a specified registry value.

7. **`winreg.SetValueEx(key, value_name, reserved, type, value)`**  
   - Sets the value of a registry entry.
   - `type`: Specifies the type (e.g., `REG_SZ`, `REG_DWORD`).

8. **`winreg.EnumKey(key, index)`**  
   - Enumerates subkeys under a registry key.

9. **`winreg.EnumValue(key, index)`**  
   - Enumerates values under a registry key.

10. **`winreg.CloseKey(key)`**  
    - Closes an open registry key.

---

### **Common Constants**
- `HKEY_CLASSES_ROOT`
- `HKEY_CURRENT_USER`
- `HKEY_LOCAL_MACHINE`
- `HKEY_USERS`
- `HKEY_CURRENT_CONFIG`

---

### **Example Usage**
```python
import winreg

# Open a key
key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion")

# Enumerate subkeys
i = 0
while True:
    try:
        subkey = winreg.EnumKey(key, i)
        print(subkey)
        i += 1
    except OSError:
        break

# Close the key
winreg.CloseKey(key)
```

Would you like help with a specific registry operation? 😊
