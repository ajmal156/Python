hy_chra =["hello" ,"python" ,"java" ,"program"]
print(hy_chra)
print(hy_chra[2:])
hy_chra.append("lemon")
print(hy_chra)
hy_chra.remove("lemon")
print(hy_chra)
print("-".join(hy_chra))
if "python" in hy_chra:
        print("I have python program.")
        hy_chra_copy =hy_chra.copy()
        print(hy_chra_copy)
        hy_chra_copy.insert(4,"good")
        print(hy_chra_copy)
        print(len(hy_chra_copy))
        for chra in hy_chra:
                print(chra)
                
                        

    