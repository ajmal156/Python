def sum_number(*args):
    if not args:
        return "No Number Provided"
    
    results =[ ]
    for i in args:
        if isinstance(i ,(int ,float)):
          results.append(i *2)
        elif isinstance(i,str):
            try:
                num =float(i)
                results.append(i* 2)
            except ValueError:
                print(f"Warning: Could not convert '{i}' to a number, skipping.")
        else:
            print (f"Warning: Skipping non_numeric input '{i}'.")

    return results


result =sum_number(6*4 ,6.78 ,"abc" ,89 ,"text" ,"number" ,"hello world python")
print(result)