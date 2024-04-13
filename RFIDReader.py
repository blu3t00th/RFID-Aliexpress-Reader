import time
import sys

def convert_to_hex(decimal):
    return hex(decimal).split('x')[-1].upper()

def main():
    while True:
        try:
            decimal = int(input("Enter a decimal number: "))
            hex_decimal = convert_to_hex(decimal)
            print(f"Hexadecimal: {hex_decimal}")

            # Save to a text file
            with open("output.txt", "a") as f:
                f.write(f"Decimal: {decimal} Hexadecimal: {hex_decimal}\n")

        except ValueError:
            print("Invalid input. Please enter a decimal number.")
        except KeyboardInterrupt:
            print("Exiting...")
            sys.exit()

if __name__ == "__main__":
    main()
