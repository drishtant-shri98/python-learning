ext = input("File Name: ").strip().lower()

if ext.endswith(".gif"):
    print("image/gif")
elif ext.endswith(".jpeg") | ext.endswith(".jpg"):
    print("image/jpeg")
elif ext.endswith(".png"):
    print("image/png")
elif ext.endswith(".pdf"):
    print("application/pdf")
elif ext.endswith(".txt"):
    print("text/plain")
elif ext.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")
