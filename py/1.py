# import csv
# import matplotlib.pyplot as plt

# def readfile(filename):
#     """
#     This function reads a CSV file from the name passed as a parameter 
#     and returns the columns in the file as arrays.
#     """
#     columns = {}
#     try:
#         with open(filename, newline='') as csvfile:
#             reader = csv.reader(csvfile)
#             headers = next(reader)
#             for header in headers:
#                 columns[header] = []
#             for row in reader:
#                 for idx, value in enumerate(row):
#                     columns[headers[idx]].append(value)
#     except FileNotFoundError:
#         print("File not found.")
#     except Exception as e:
#         print(f"An error occurred: {e}")
#     return columns

# def main():
#     """
#     Main function to call all other functions for the required output
#     """
#     filename = input("Enter file name or: ")
#     data = readfile(filename)
#     if data:
#         # Now 'data' contains the columns as arrays, you can use them as needed
        
#         # Example usage to print the data
#         for key, value in data.items():
#             print(f"{key}: {value}")
        
#         # Plotting example (you may need to modify this based on your data)
#         plt.plot(data['X'], data['Y'])
#         plt.xlabel('X Axis')
#         plt.ylabel('Y Axis')
#         plt.title('Plotting CSV Data')
#         plt.show()

# if __name__ == "__main__":
#     main()


import csv

def readfile(filename):
    """
    This function reads a CSV file from the name passed as a parameter 
    and returns the columns in the file as arrays.
    """
    columns = {}
    try:
        with open(filename, newline='') as csvfile:
            reader = csv.reader(csvfile)
            headers = next(reader)
            for header in headers:
                columns[header] = []
            for row in reader:
                for idx, value in enumerate(row):
                    columns[headers[idx]].append(value)
    except FileNotFoundError:
        print("File not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    return columns

def write_to_csv(data, output_filename):
    """
    This function writes the data to a CSV file.
    """
    try:
        with open(output_filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(data.keys())  # Write headers
            writer.writerows(zip(*data.values()))  # Write values
        print(f"Data written to {output_filename} successfully.")
    except Exception as e:
        print(f"An error occurred while writing to {output_filename}: {e}")

def main():
    """
    Main function to call all other functions for the required output
    """
    filename = input("Enter input file name: ")
    data = readfile(filename)
    if data:
        # Now 'data' contains the columns as arrays, you can use them as needed
        
        # Example usage to print the data
        for key, value in data.items():
            print(f"{key}: {value}")
        
        output_filename = input("Enter output file name: ")
        write_to_csv(data, output_filename)

if __name__ == "__main__":
    main()

