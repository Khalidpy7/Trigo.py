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
    
