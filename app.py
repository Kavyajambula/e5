def is_palindrome(word:str)->bool:
    cleaned = word.lower().replace(" ","")
    return cleaned[::-1]==cleaned

if __name__ == "__main__":
    word = input("Enter:")
    if is_palindrome(word):
        print(f"{word} is a palindrome")
    else:   
        print(f"{word} is not a palindrome")