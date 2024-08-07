char_type =["book" ,"pincel" "pin" ,"copy"]
default_value ="bag"
new_dict =dict.fromkeys(char_type ,default_value)
print(new_dict)
cube_num ={g:g**3 for g in range(6)}
print(cube_num)
top_type ={
    "topic":{"program":"python" ,"world":"citys"},
    "explain":{"java":"html" ,"qure":"git"},
}
print(top_type["topic"]["program"])
print(top_type["topic"])
print(top_type["explain"])
pip_type ={"get":"out" ,"fit":"hub" ,"name":"diffrent"}
print(pip_type)
print(pip_type["get"])
print(pip_type.get("name"))
pip_type["index"] ="value"
print(pip_type)
print(pip_type.pop("fit"))
print(pip_type.popitem())
print(pip_type)
for char in pip_type:
    print(char, pip_type[char])
    if "formate" in pip_type:
        print("yes we are avalibal key")
        print(char_type.clear())
      