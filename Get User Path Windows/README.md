To get the path of the current user's directory (like `C:\Users\windows_rig2`) on a Windows OS, you can use environment variables in various programming languages or through the command line.

Here are a few options:

### 1. **Using Command Line (CMD)**
You can use the following command to get the path:
```bash
echo %USERPROFILE%
```

This will return something like `C:\Users\your_username`.

### 2. **Using PowerShell**
In PowerShell, you can retrieve the user's profile path using:
```powershell
$env:USERPROFILE
```

### 3. **Using Python**
If you're working with Python, you can get the current user's home directory like this:
```python
import os
user_path = os.path.expanduser('~')
print(user_path)
```

### 4. **Using C#**
If you're working in C#, you can use the following code:
```csharp
string userPath = Environment.GetFolderPath(Environment.SpecialFolder.UserProfile);
Console.WriteLine(userPath);
```

These methods will all return the path to the current user's directory on a Windows machine.