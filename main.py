def obsah_obdelniku():
    while(True):
        try:
            a = float(input("Zadej stranu a: "))
            b = float(input("Zadej stranu b: "))

            print(f"Obsah je: {abs(a*b)}")
        except:
            print("Neplatný vstup")
        else:
            break
    
        
obsah_obdelniku()