def obsah_obdelniku():
    while(True):
        a = input("Zadej stranu a: ")
        if(not a.isdigit()):
            print("Neplatný vstup")
            continue
        b = input("Zadej stranu b: ")
        if(not b.isdigit()):
            print("Neplatný vstup")
            continue

        print(int(a)*int(b))
        break
        
obsah_obdelniku()