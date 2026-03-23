from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import pandas as pd

file_path = input("Enter file path of the CSV: ").strip().strip('"')
try:
    csv = pd.read_csv(file_path)
except Exception as e:
    print("Error while reading the CSV File", e)
    quit()
print("Available Columns:")
for col in csv.columns:
    print("-", col)
x_column = input("From the list choose the Independent Variable: ").strip()
y_column = input("From the list coose the Depndent Variable: ").strip()

if x_column in csv.columns and y_column in csv.columns:
    x_value = csv[[x_column]]
    y_value = csv[y_column]
    model = LinearRegression()
    model.fit(x_value, y_value)
    predictions = model.predict(x_value)
else:
    print("Columns not available")
    quit()

while True:
    try:
        user_choice = int(input(f"""Enter what do you want to do with the provided data:
                                1| Print General Overview of the CSV
                                2| Plot the Graph of {x_column} vs {y_column}
                                3| Perform Linear Regression on the Data
                                4| Perform Linear Regression and compare the graph between Original Data and Best-fit Line
                                5| Using Linear Regression check predicted {y_column} for given {x_column}
                                6| Enter the {x_column} to get predicted {y_column} and add them to a newly named CSV file
                                7| Exit
                                """))
    except:
        print("Enter a number")
        continue
    if user_choice == 1:
        print("First 5 rows: ",csv.head())
        print("Last 5 rows: ", csv.tail())
        print(csv.shape)
        print(csv.columns)
        print(csv.describe())
        print(csv.dtypes)

    elif user_choice == 2:
        plt.scatter(x_value, y_value, color = "green", label = "Original Data")
        plt.title("Original Graph for the data ")
        plt.xlabel(x_column)
        plt.ylabel(y_column)
        plt.legend()
        plt.show()

    elif user_choice == 3:
        print("From training the model we get the following informations")
        print("Slope: ", model.coef_[0])
        print("Intercept: ", model.intercept_)
        print("Model Accuracy = ", model.score(x_value, y_value))

    elif user_choice == 4:
        plt.scatter(x_value, y_value , color = "orange" , label = "Original Data")
        plt.plot(x_value, predictions , color = "red" , label = "Best-fit line")
        plt.xlabel(x_column)
        plt.ylabel(y_column)
        plt.legend()
        plt.show()

    elif user_choice == 5:
        new_x_values = float(input(f"Enter the new {x_column} value: "))
        predicted_y_value = model.predict([[new_x_values]])
        print(f"For {new_x_values} {x_column}, predicted {y_column} is {predicted_y_value[0]}")

    elif user_choice == 6:
        new_file_name = input("Enter output file name: ").strip() + ".csv"

        csv["Predicted_" + y_column] = predictions

        csv.to_csv(new_file_name, index=False)
        print(f"File saved as {new_file_name}")

    elif user_choice == 7:
        break
    
    else:
        break
