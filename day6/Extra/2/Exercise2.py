def celsius_to_fahrenheit(input_file, output_file):
    try:
        with open(input_file, "r", encoding="utf-8") as infile:
            lines = infile.readlines()

        results = []

        for line in lines:
            line = line.strip()
            if not line:
                continue 
            try:
                celsius = float(line)
                fahrenheit = (celsius * 9/5) + 32
                results.append(f"{celsius:.2f}C = {fahrenheit:.2f}F")
            except ValueError:
                print(f"Skipping invalid temperature: '{line}'")

        with open(output_file, "w", encoding="utf-8") as outfile:
            for result in results:
                outfile.write(result + "\n")

        print(f"Conversion complete. Results written to '{output_file}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except PermissionError:
        print(f"Error: You don't have permission to read/write the files.")
    except Exception as e:
        print(f"Unexpected error: {e}")



input_file = "celsius.txt"
output_file = "fahrenheit.txt"


celsius_to_fahrenheit(input_file, output_file)
