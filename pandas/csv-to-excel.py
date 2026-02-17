import pandas as pd 


# Load the CSV file
csv_file_path = '/Users/$(whoami)/Downloads/2025-11-06-input.csv'  
data = pd.read_csv(csv_file_path, sep=',', encoding='utf-8', on_bad_lines='skip')  

# Display the first few rows of the dataframe (optional)  
print(data.head())  

# Save the DataFrame to an Excel file  
excel_file_path = '/Users/$(whoami)/Downloads/2025-11-06-output.xlsx'  
data.to_excel(excel_file_path, index=False)  

print(f'Data has been successfully saved to {excel_file_path}')