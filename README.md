# 🔢 Trigonometry Values Calculator

A simple command-line Python tool for calculating **trigonometric ratios, inverse trigonometric angles, and the hypotenuse of a right triangle**.

The original program uses Python's built-in `math` module and the third-party `termcolor` package for colored terminal output. fileciteturn0file0L1-L2

---

# ⚠️ STEP 1 — READ BEFORE USING

> [!WARNING]
> This is a **simple educational calculator**, not a fully validated scientific calculator.

Please read these limitations before running the program:

### 1. Invalid input can terminate the program
The current program expects correctly formatted input. Entering text where a number is expected can produce a Python error.

### 2. Domain restrictions apply
Inverse trigonometric functions have mathematical domain restrictions:

- `arcsin(x)` requires `-1 ≤ x ≤ 1`
- `arccos(x)` requires `-1 ≤ x ≤ 1`
- `arcsec(x)` requires `|x| ≥ 1`
- `arccosec(x)` requires `|x| ≥ 1`

The current source does not explicitly validate these conditions before calling the corresponding `math` functions. fileciteturn0file0L90-L107

### 3. Division by zero is possible
`cot`, `sec`, and `cosec` use reciprocal operations. Certain angles can therefore cause a division-by-zero error. fileciteturn0file0L59-L67

### 4. Precision is limited
Several direct trigonometric results are rounded to **3 decimal places** before being displayed. fileciteturn0file0L50-L67

### 5. Angle convention
Direct trigonometric calculations use the supplied angle in **degrees** and convert it to radians internally. fileciteturn0file0L50-L58

### 6. Inverse-function convention
The program implements:

```text
arccot(x)   → atan(1/x)
arcsec(x)   → acos(1/x)
arccosec(x) → asin(1/x)
```

These represent the conventions chosen by this program and do not cover every possible inverse-trigonometric branch. fileciteturn0file0L100-L107

---

# 🛠️ STEP 2 — REQUIREMENTS

## Python

Install **Python 3.x**.

Check your Python installation:

```bash
python --version
```

or:

```bash
python3 --version
```

## Required package

Install:

```text
termcolor
```

The program imports it with:

```python
from termcolor import colored as tc
```

Python's `math` module is built into Python, so it does **not** need a separate installation. fileciteturn0file0L1-L2

---

# 📁 STEP 3 — REPOSITORY STRUCTURE

```text
trigonometry-calculator/
├── am.py
├── README.md
└── requirements.txt
```

| File | Purpose |
|---|---|
| `am.py` | Main calculator program |
| `README.md` | Project documentation |
| `requirements.txt` | Required third-party package |

---

# 📦 STEP 4 — INSTALL THE DEPENDENCY

Open a terminal inside the project folder.

Install `termcolor`:

```bash
pip install termcolor
```

If your system uses `pip3`:

```bash
pip3 install termcolor
```

Or install from the included requirements file:

```bash
pip install -r requirements.txt
```

---

# ▶️ STEP 5 — RUN THE PROGRAM

Run:

```bash
python am.py
```

or:

```bash
python3 am.py
```

The program first displays its banner and asks whether you want to continue. fileciteturn0file0L129-L131

When prompted, enter:

```text
y
```

---

# 🎮 STEP 6 — CHOOSE A CALCULATION MODE

After starting the program, choose one of these modes:

```text
(a) find trignometric ratio.
(b) find angle.
(c) Pythagoric calculations.
```

fileciteturn0file0L21-L34

---

# 🧮 STEP 7 — USE THE CALCULATOR

## A. Trigonometric Ratios

Choose:

```text
a
```

Available ratios:

```text
(1) sinθ
(2) cosθ
(3) tanθ
(4) cotθ
(5) secθ
(6) cosecθ
```

fileciteturn0file0L38-L47

### Example: sin 45°

Enter:

```text
1 45
```

This means:

```text
sin 45°
```

The program converts the degree angle to radians and calculates the value using Python's trigonometric functions. fileciteturn0file0L50-L52

---

## B. Find an Angle

Choose:

```text
b
```

Available functions:

```text
(1) arcsin(x)
(2) arccos(x)
(3) arctan(x)
(4) arccot(x)
(5) arcsec(x)
(6) arccosec(x)
```

fileciteturn0file0L75-L84

### Example: arcsin(0.5)

Enter:

```text
1 0.5
```

The result is displayed in degrees. fileciteturn0file0L90-L92

---

## C. Pythagorean Calculation

Choose:

```text
c
```

Enter:

```text
height base
```

For example:

```text
3 4
```

The program calculates:

```text
hypotenuse = √(height² + base²)
```

Result:

```text
hypotenuse = 5.0
```

The calculation is implemented using the square-root calculation in the source. fileciteturn0file0L116-L126

---

# 🔐 STEP 8 — USAGE NOTE

This program performs mathematical calculations locally on your computer.

After `termcolor` has been installed, it does not require an internet connection to perform its calculations.

Do not rely on its output when high numerical precision or specialized mathematical software is required.

---

# ✨ FEATURES

The program provides three main calculation modes:

1. **Trigonometric ratios**
   - `sin θ`
   - `cos θ`
   - `tan θ`
   - `cot θ`
   - `sec θ`
   - `cosec θ`

2. **Inverse trigonometric functions**
   - `arcsin(x)`
   - `arccos(x)`
   - `arctan(x)`
   - `arccot(x)`
   - `arcsec(x)`
   - `arccosec(x)`

3. **Pythagorean calculation**
   - Calculates the hypotenuse from height and base.

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



---

# 🚀 POSSIBLE IMPROVEMENTS

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

# 📜 LICENSE

No license was specified in the supplied source.

Add a license file before publishing the repository publicly if you want to define how others may use, modify, or redistribute the project.
