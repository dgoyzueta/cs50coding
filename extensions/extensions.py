# Program: extensions.py

def main():
    file_name = input("Enter file name with its extension: ")

    file_name = file_name.strip().lower()
    extension = file_name[file_name.rfind("."):]

    match extension:
        case ".gif":
            print("image/gif")
        case ".jpg" | ".jpeg":
            print("image/jpeg")
        case ".png":
            print("image/png")
        case ".pdf":
            print("application/pdf")
        case ".txt":
            print("text/plain")
        case ".zip":
            print("application/zip")
        case _:
            print("application/octet-stream")

main()
