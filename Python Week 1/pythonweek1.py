name = input("What is your name? ")

#parts of a typical print: print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
#objects = how many things you want to print
#sep = what to put between the objects (default is a space ' ')
#end = what to put at the end (default is a newline '\n')

name = name.strip()  # Remove any leading/trailing whitespace
name = name.lower()  # Convert to lowercase
name = name.title()  # Capitalize the first letter

print("Hello, ", end = '')
print(name, sep = "...", end = '!\n')
