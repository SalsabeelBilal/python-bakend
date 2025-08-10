def palindrome_checker(input_file, output_file):
    try:
        with open(input_file, "r", encoding="utf-8") as infile:
            words = [line.strip() for line in infile if line.strip()]
        
    
        palindromes = [word.upper() for word in words if word.lower() == word.lower()[::-1]]

        
        if palindromes:
            print("Palindromes found:")
            for word in palindromes:
                print(word)
        else:
            print("No palindromes found.")

        with open(output_file, "w", encoding="utf-8") as outfile:
            for word in palindromes:
                outfile.write(word + "\n")

        print(f"Palindromes have been written to '{output_file}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except PermissionError:
        print(f"Error: You don't have permission to read/write the files.")
    except Exception as e:
        print(f"Unexpected error: {e}")


input_file = "input_words.txt"
output_file = "palindromes.txt"
palindrome_checker(input_file, output_file)
