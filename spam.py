import pandas as pd

def convert_to_csv(input_file='SMSSpamCollection', output_file='spam.csv'):
    try:
        # Read the raw data file with tab separator
        df = pd.read_csv(input_file, sep='\t', header=None, names=['label', 'message'])

        # Display the first few rows of the DataFrame for verification
        print("Initial DataFrame:")
        print(df.head())  # Show the first few rows of the DataFrame

        # Check the shape of the DataFrame
        print("DataFrame Shape:", df.shape)

        # Ensure there are exactly 2 columns
        if df.shape[1] != 2:
            print("Error: The input file does not have exactly two columns.")
            return
        
        # Save it as spam.csv in the correct format
        df.to_csv(output_file, index=False, quoting=1)  # quoting=1 is equivalent to csv.QUOTE_ALL
        print(f"Converted {input_file} to {output_file} successfully!")
    
    except FileNotFoundError:
        print(f"Error: The file {input_file} was not found. Please ensure the file is in the current directory.")
    except pd.errors.ParserError:
        print("Error: Could not parse the file. Please check the format of the input file.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function to convert the dataset
convert_to_csv()
import pandas as pd
df = pd.read_csv('spam.csv')
print(df.head())

df.to_csv('spam.csv', index=False, quoting=0)  # quoting=0 means no quotes