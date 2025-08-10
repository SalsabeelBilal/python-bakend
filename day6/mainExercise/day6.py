def count_word_frequency(file_path):
    word_count = {}
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                words = line.lower().split()
                for word in words:
                    word_count[word] = word_count.get(word, 0) + 1
        for word, count in sorted(word_count.items()):
            print(f"{word}: {count}")
    except FileNotFoundError:
        print(f"{file_path} does not exist.")
    except PermissionError:
        print(f"You don't have permission to read {file_path}")
    except Exception as e:
        print(f"error: {e}")


file_name = "test.txt"
count_word_frequency(file_name)