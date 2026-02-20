# <h1 align="center">🖥️ Terminal Visuals Suite</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Platform-Windows%20Console-blue?style=flat-square">
  <img src="https://img.shields.io/badge/Rendering-Native%20Win32%20Blitting-orange?style=flat-square">
  <img src="https://img.shields.io/badge/Language-Python%20(ctypes)-green?style=flat-square">
  <img src="https://img.shields.io/badge/License-MIT-lightgrey?style=flat-square">
</p>

<p align="center">
  <b>High-Performance Real-Time Terminal Visualizers for Windows</b><br>
  Lightweight. Flicker-Free. Zero Dependencies.
</p>

---

## ✨ Overview

**Terminal Visuals Suite** is a polished collection of real-time visual effects built exclusively for the **Windows Console**.

Unlike traditional terminal applications that rely on standard output streams, this suite renders directly to the console buffer using the **native Win32 API**. The result:

- Smooth animation
- Zero flicker
- Minimal CPU usage
- Instant startup
- No runtime dependencies

Designed as a finished product — download and run.

---

## 🎬 Visual Modules

| Rusty Rain | Cyber Clock | Pipes |
|:--:|:--:|:--:|
| ![Rusty Rain](./pic/matrix.png) | ![Cyber Clock](./pic/clock.png) | ![Pipes](./pic/pipes.png) |

### 🟢 Rusty Rain
A high-speed matrix-style character rain with customizable palettes.

### 🔵 Cyber Clock
A stylized digital clock with animated visual framing.

### 🟣 Pipes
A dynamic procedural pipe simulation with reset capability.

---

## ⚙️ Rendering Engine

Terminal Visuals Suite uses:

- Native **Win32 Console API**
- Direct buffer manipulation
- Manual frame blitting
- High refresh render loop
- Zero stdout streaming

This architecture ensures stable, high-FPS animation inside the Windows Console environment.

No flicker. No redraw artifacts. No hacks.

---

## 🚀 Installation

No installation required.

Download the `.exe` files and run.

```
RustyRain.exe
CyberClock.exe
PipesMatrix.exe
```

Portable. Standalone. Ready to use.

---

## 🎮 Controls

| Key | Function |
|------|----------|
| → (Right Arrow) | Next theme |
| ← (Left Arrow) | Previous theme |
| R | Reset simulation (Pipes only) |
| Q | Exit |
| Esc | Exit |

The console state is automatically restored on exit.

---

## 🎨 Dynamic Theme Engine

Switch visual styles instantly at runtime.

Available palettes include:

- Deep Sea (Default)
- Classic Matrix
- Cyber Hell
- Synthwave
- Fallout
- Additional custom palettes

### Theme Preview

| Deep Sea | Classic Matrix | Cyber Hell | Synthwave | Fallout |
|:--:|:--:|:--:|:--:|:--:|
| ![Deep Sea](./pic/1.png) | ![Classic Matrix](./pic/2.png) | ![Cyber Hell](./pic/3.png) | ![Synthwave](./pic/4.png) | ![Fallout](./pic/5.png) |

Switch using:

```
←   →
```

---

## ⚡ Performance

- CPU usage typically under **1%**
- No background services
- No external libraries
- No Python runtime required (compiled executable)

Optimized for responsiveness and long runtime sessions.

---

## 🖥️ PowerShell Quick Access (Optional)

Add aliases to your PowerShell profile for instant launch:

```powershell
$Path = "D:\Program\Miniapp"  # Update this path
Set-Alias mx "$Path\RustyRain.exe"
Set-Alias cl "$Path\CyberClock.exe"
Set-Alias pp "$Path\PipesMatrix.exe"
```

Reload PowerShell.

Then simply run:

```
mx   # Rusty Rain
cl   # Cyber Clock
pp   # Pipes
```

---

## 🛠️ Technology Stack

- Python
- ctypes (standard library only)
- Native Win32 Console API
- Blitting-based rendering pipeline

No frameworks. No graphics libraries. Pure console control.

---

## 📦 System Requirements

- Windows 10 / 11
- Standard Windows Console or Windows Terminal
- No additional dependencies

---

## 📄 License

Distributed under the MIT License.

See [LICENSE](./LICENSE) for details.

---

<p align="center">
  Crafted for developers and terminal enthusiasts who believe the console deserves performance and style.
</p>
