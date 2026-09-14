# 🔢 Trigonometry Values Calculator

A simple command-line Python tool for calculating **trigonometric ratios, inverse trigonometric angles, and the hypotenuse of a right triangle**.

The original program uses Python's built-in `math` module and the third-party `termcolor` package for colored terminal output. fileciteturn0file0L1-L2

---

## 📁 Repository Structure

```text
trigonometry-calculator/
├── am.py
├── README.md
└── requirements.txt
```

### Files

| File | Purpose |
|---|---|
| `am.py` | Main calculator program |
| `README.md` | Project documentation |
| `requirements.txt` | Required third-party package |

---

## ✨ Features

The program provides three calculation modes:

### 1. Trigonometric Ratios

You can calculate:

- `sin θ`
- `cos θ`
- `tan θ`
- `cot θ`
- `sec θ`
- `cosec θ`

The program accepts the angle in **degrees**.

Example:

```text
1 45
```

means:

```text
sin 45°
```

The six ratio choices are defined in the program's menu. fileciteturn0file0L38-L47

### 2. Inverse Trigonometric Functions

You can calculate:

- `arcsin(x)`
- `arccos(x)`
- `arctan(x)`
- `arccot(x)`
- `arcsec(x)`
- `arccosec(x)`

The result is displayed in degrees. fileciteturn0file0L75-L84

### 3. Pythagorean Calculation

Enter the **height** and **base**, and the program calculates the hypotenuse using:

```text
hypotenuse = √(height² + base²)
```

The calculation is implemented near the end of the program. fileciteturn0file0L116-L126

---

# 🛠️ Requirements

## Python

Install **Python 3.x**.

Check whether Python is installed:

```bash
python --version
```

or:

```bash
python3 --version
```

## Python Package

The only external package required by the current source code is:

```text
termcolor
```

The program imports it as:

```python
from termcolor import colored as tc
```

while `math` is part of Python's standard library and does not need to be installed separately. fileciteturn0file0L1-L2

---

# 📦 Installation

Clone or download the repository, then open a terminal inside the project folder.

Install the dependency:

```bash
pip install termcolor
```

If your system uses `pip3`:

```bash
pip3 install termcolor
```

You can also install everything from `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

# ▶️ How to Execute

Run:

```bash
python am.py
```

or:

```bash
python3 am.py
```

The program first displays its banner and asks whether you want to continue. fileciteturn0file0L129-L131

Enter:

```text
y
```

Then select one of the available modes:

```text
(a) find trignometric ratio.
(b) find angle.
(c) Pythagoric calculations.
```

fileciteturn0file0L21-L34

---

# 🧮 Examples

## Example 1 — sin 45°

Select:

```text
a
```

Then choose:

```text
1 45
```

The program calculates the sine value using Python's `math.sin()` and degree-to-radian conversion. fileciteturn0file0L50-L52

---

## Example 2 — arcsin(0.5)

Select:

```text
b
```

Then enter:

```text
1 0.5
```

The program uses `math.asin()` and converts the result from radians to degrees. fileciteturn0file0L90-L92

---

## Example 3 — Hypotenuse

Select:

```text
c
```

Then enter:

```text
3 4
```

The result will be approximately:

```text
hypotenuse = 5.0
```

---

# ⚠️ Limitations & Warnings

> [!WARNING]
> This is a **simple educational calculator**, not a fully validated scientific calculator.

### 1. Invalid input can terminate the program

The current program expects correctly formatted input. For example, entering text where a number is expected can produce a Python error.

### 2. Domain restrictions apply

Inverse trigonometric functions have mathematical domain restrictions.

For example:

- `arcsin(x)` requires `-1 ≤ x ≤ 1`
- `arccos(x)` requires `-1 ≤ x ≤ 1`
- `arcsec(x)` requires `|x| ≥ 1`
- `arccosec(x)` requires `|x| ≥ 1`

The current source does not explicitly validate these conditions before calling the corresponding `math` functions. fileciteturn0file0L90-L107

### 3. Division by zero is possible

`cot`, `sec`, and `cosec` are calculated using reciprocal operations. Values at which the corresponding denominator becomes zero can therefore cause a division-by-zero error. fileciteturn0file0L59-L67

### 4. Precision is limited

Several direct trigonometric results are rounded to **3 decimal places** before being displayed. fileciteturn0file0L50-L67

### 5. Angle convention

The direct trigonometric calculations convert the supplied degree value to radians before using Python's trigonometric functions. fileciteturn0file0L50-L58

### 6. `arccot`, `arcsec`, and `arccosec` conventions

The inverse functions for these ratios are implemented through reciprocal relationships:

```text
arccot(x)  → atan(1/x)
arcsec(x)  → acos(1/x)
arccosec(x) → asin(1/x)
```

These implementations should be treated as the program's chosen convention rather than a complete treatment of all possible inverse-trigonometric branches. fileciteturn0file0L100-L107

---

# 🔐 Safety / Usage Note

This program performs mathematical calculations locally on your computer. It does not require an internet connection after the required Python package has been installed.

Do not treat its output as authoritative when high numerical precision or specialized mathematical software is required.

---

# 🧑‍💻 Source Code

The following is the original `am.py` source supplied for this repository:

```python
from termcolor import colored as tc
import math
#from fractions import Fraction

def banner():
    tool_banner='''
    
████████╗██████╗ ██╗ ██████╗  ██████╗ 
╚══██╔══╝██╔══██╗██║██╔════╝ ██╔═══██╗
   ██║   ██████╔╝██║██║  ███╗██║   ██║
   ██║   ██╔══██╗██║██║   ██║██║   ██║
   ██║   ██║  ██║██║╚██████╔╝╚██████╔╝
   ╚═╝   ╚═╝  ╚═╝╚═╝ ╚═════╝  ╚═════╝                                
    '''
    print(tc(tool_banner, "light_blue"))
    
def permis():
    global permis
    permis=input(tc("[?] want to continue [y/n] : ", "light_yellow"))
    
def check_user_permis():
    if permis=="y":
        while True:
            print()
            print(tc("[*] caption :", "light_green"), tc("this tool is made for simple trignometric calculation.", "light_cyan"))
            
            selector=input(tc('''         
   (a) find trignometric ratio.
   (b) find angle.
   (c) Pythagoric calculations.
    
[?] select one in all |> ''',"light_grey"))
            
            if selector=="a":
                print()
                print(tc(" TRIGNOMETRIC RATIO ", "light_yellow", "on_light_blue"))  
                print()
                print(tc(" USE ", "light_green", "on_light_yellow"), tc(": if I calc. sin 45, then input like as [number][space][angle] = 1 45", "light_cyan"))
                ratio,angle=map(int, input(tc('''
         (1) sinθ
         (2) cosθ
         (3) tanθ
         (4) cotθ
         (5) secθ
         (6) cosecθ
                
    [?] which you want to calc.: ''', "light_grey")).split())
                print()    
                
                if ratio==1:
                    sin_result=round(math.sin(math.radians(-angle)),3)
                    print(tc(f"[r] sin{angle} = {-(sin_result)}", "light_yellow"))
                elif ratio==2:
                    cos_result=round(math.cos(math.radians(-angle)),3)
                    print(tc(f"[r] cos{angle} = {-(cos_result)}", "light_yellow"))
                elif ratio==3:
                    tan_result=round(math.tan(math.radians(-angle)),3)
                    print(tc(f"[r] tan{angle} = {-(tan_result)}", "light_yellow"))
                elif ratio==4:
                    cot_result=1/round(math.tan(math.radians(-angle)),3)
                    print(tc(f"[r] cot{angle} = {-(cot_result)}", "light_yellow"))
                elif ratio==5:
                    sec_result=1/round(math.cos(math.radians(-angle)),3)
                    print(tc(f"[r] sec{angle} = {-(sec_result)}", "light_yellow"))
                elif ratio==6:
                    cosec_result=1/round(math.sin(math.radians(-angle)),3)
                    print(tc(f"[r] cosec{angle} = {-(cosec_result)}", "light_yellow"))
                else:
                    print(tc("[!] Program intrupted !!", "light_red"))
                    break
            elif selector=="b":
                print()
                print(tc(" FIND ANGLE ", "light_yellow", "on_light_red")) 
                print()
                print(tc(" USE ", "light_blue", "on_light_yellow"), tc(": if I calc. asin 1/2, then input like as [number][space][valu3] = 1 0.5", "light_cyan"))
                ratio,value=input(tc('''
         (1) arcsin(x)
         (2) arccos(x)
         (3) arctan(x)
         (4) arccot(x)
         (5) arcsec(x)
         (6) arccoesc(x)
                
    [?] which you want to calc.: ''', "light_grey")).split()
    
                print()
                ratio=int(ratio)
                value=float(value)
                
                if ratio==1:
                    arcsin_r=round(math.degrees(math.asin(value)))
                    print(tc(f"[r] arcsin {value} = {arcsin_r}°", "light_yellow"))
                    
                elif ratio==2:
                    arccos_r=round(math.degrees(math.acos(value)))
                    print(tc(f"[r] arccos {value} = {arccos_r}°", "light_yellow"))
                elif ratio==3:
                    arctan_r=round(math.degrees(math.atan(value)))
                    print(tc(f"[r] arctan {value} = {arctan_r}°", "light_yellow"))
                elif ratio==4:
                    arccot_r=round(math.degrees(math.atan(1/value)))
                    print(tc(f"[r] arccot {value} = {arccot_r}°", "light_yellow"))
                elif ratio==5:
                    arcsec_r=round(math.degrees(math.acos(1/value)))
                    print(tc(f"[r] arcsec {value} = {arcsec_r}°", "light_yellow"))
                elif ratio==6:
                    arccosec_r=round(math.degrees(math.asin(1/value)))
                    print(tc(f"[r] arccosec {value} = {arccosec_r}°", "light_yellow"))
                else:
                    print(tc("[!] Program intrupted !!", "light_red"))
                    
            elif selector=="c":
                print()
                print(tc(" PYTHAGORIC CALCULATION ", "light_yellow", "on_light_red")) 
                print()
                print(tc(" USE ", "light_blue", "on_light_yellow"), tc(" : if I want to calculate Hypotenuse then enter values like [height] [base]", "light_cyan"))
                print()
                height, base=map(float, input(tc(" [?] input values : ", "light_yellow")).split())
                
                a=height*height
                b=base*base
                
                x=a+b
                hypo_r=math.sqrt(x)
                print()
                print(tc(f"[r] hypotenuse = {hypo_r}", "light_yellow"))
                
               
banner()
permis()
check_user_permis()
```

---

# 🚀 Possible Improvements

Future versions could add:

- Input validation
- Error handling with `try/except`
- Division-by-zero protection
- Domain validation for inverse functions
- A quit option inside the calculator menu
- Better spelling and menu formatting
- More accurate handling of `cot`, `sec`, and `cosec`
- Support for radians
- More Pythagorean calculations, such as finding a missing side
- Automated tests
- A graphical user interface

---

## 📜 License

No license was specified in the supplied source. Add a license file before publishing the repository publicly if you want to define how others may use, modify, or redistribute the project.
