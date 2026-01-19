def main():
    name = input("what's name of a file ?").lower().strip()
    before, dot, after = name.rpartition(".")
    extension(name, before, after)

def extension(name, before, after):
    if name.endswith(('.gif','.jpeg','.png')):
        print(f"image/{after}")
    elif name.endswith('.jpg'):
        print(f"image/jpeg")
    elif name.endswith(('.pdf','.zip')):
        print(f"application/{after}")
    elif name.endswith('.txt'):
        print(f"text/plain")
    else:
        print("application/octet-stream")

main()
