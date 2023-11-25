my_dict = {"key1":"value1","key2": "value2"}

my_dict["key3"] = "value3"

del my_dict["key2"]
for k,v in my_dict.items():
    print(k)
    print(v)
    print("--------")