import os

ENTRY = '"Sorry, I\'m full," I said to the guy holding the door open. He stepped out. I was empty. I just didn\'t like him.'

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
