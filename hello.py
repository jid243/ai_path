# hello.py
def greet(name: str) -> str:
    return f"hello, {name}!"

if __name__ == "__main__":
    name = input("Enter your name: ")
    print(greet(name))
