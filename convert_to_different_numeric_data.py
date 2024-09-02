user_input = input("Enter a number: ")

# Convert input to different numeric data types
try:
    # Convert to integer
    integer_value = int(user_input)
    print(f"Integer value: {integer_value}")
except ValueError:
    print("Invalid input for integer conversion.")

try:
    # Convert to float
    float_value = float(user_input)
    print(f"Float value: {float_value}")
except ValueError:
    print("Invalid input for float conversion.")

try:
    # Convert to complex
    complex_value = complex(user_input)
    print(f"Complex value: {complex_value}")
except ValueError:
    print("Invalid input for complex conversion.")


# In[ ]:


#Integer ( int ): represents positive or negative whole numbers like 3 or -512. 
#Floating point number ( float ): represents real numbers like 3.14159 or -2.5. 
#Complex :consists of two values, the first one is the real part of the complex number, and the second one is the imaginary part of the complex numbe


