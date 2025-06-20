string ="123-456-789-012"
# string_name[start:end:step]
print(f" \"{string[0:3]}\" is the string from start to positon 3")
# "-" does not include in the output 
print(f" \"{string[: :2]}\" is the string at step 2" )
#python will understand the starting and ending 
print(f" \"{string[: :-2]}\" is the string at step -2 from another direction")
print(f" \"{string[: :-1]}\" is the string at step -1 which will ultimately reverse the whole string")
print(f" XXX-XXX-XXX-{string[12:]}")

last_digits = string[-3:]
print(f"XXX-XXX-XXX-{last_digits}")
