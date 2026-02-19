Terminal Visuals Suite
A collection of high-performance, lightweight terminal visualizers built for the Windows Console using native Win32 API Blitting

📸 Previews
Rusty Rain,Cyber Clock,Pipes
,,

✨ Core Features
Native Win32 Rendering: Bypasses standard I/O for high-speed, flicker-free updates.

Dynamic Palettes: Switch between various color themes (Classic, Synthwave, Cyber Hell, etc.) in real-time.

Resource Efficient: Written in Python using ctypes (standard library), resulting in < 1% CPU usage.

Portable: Standalone executables—no Python installation required.

⌨️ Controls
Interact with the visuals using the following keys:

Right Arrow (→): Switch to the next color palette.

Left Arrow (←): Switch to the previous color palette.

R: Reset the simulation (Pipes only).

Q or Esc: Safely exit and restore console state.

🚀 Usage
Simply run the .exe

PowerShell Integration
To access these tools quickly from anywhere, add the following aliases to your PowerShell $PROFILE:
$Path = "D:\Program\Miniapp" # Change this to your folder path
Set-Alias mx "$Path\RustyRain.exe"
Set-Alias cl "$Path\CyberClock.exe"
Set-Alias pp "$Path\PipesMatrix.exe"