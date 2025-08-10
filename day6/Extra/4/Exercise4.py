def analyze_log(input_file, output_file):
    try:
        with open(input_file, "r", encoding="utf-8") as infile:
            lines = infile.readlines()

        status_counts = {200: 0, 404: 0, 500: 0}

        for line in lines:
            parts = line.strip().split()
            if len(parts) < 3:
                print(f"Skipping malformed line: {line.strip()}")
                continue  

            try:
                status = int(parts[1])  
                if status in status_counts:
                    status_counts[status] += 1
            except ValueError:
                print(f"Skipping invalid status code in line: {line.strip()}")

        with open(output_file, "w", encoding="utf-8") as outfile:
            outfile.write(f"Successful (200): {status_counts[200]}\n")
            outfile.write(f"Not Found (404): {status_counts[404]}\n")
            outfile.write(f"Server Error (500): {status_counts[500]}\n")

        print(f"Log analysis complete. Report saved to '{output_file}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except PermissionError:
        print(f"Error: You don't have permission to read/write the files.")
    except Exception as e:
        print(f"Unexpected error: {e}")



input_file = "server.log"
output_file = "report.txt"


analyze_log(input_file, output_file)
