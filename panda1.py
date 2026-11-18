# # import pandas as pd
# # import matplotlib.pyplot as plt

# # # Create a DataFrame
# # data = {
# #     "Name": ["Rahul", "Aman", "Priya"],
# #     "Marks": [85, 90, 88],
# #     "City": ["Delhi", "Chandigarh", "Mohali"]
# # }
# # df = pd.DataFrame(data)
# # # Display the data
# # print(df)

# # plt.bar(df["Name"], df["Marks"])
# # plt.title("Student Marks")
# # plt.xlabel("Student Name")
# # plt.ylabel("Marks")
# # plt.show()


# import pandas as pd
# import matplotlib.pyplot as plt

# # Create a DataFrame
# data = {
#     "Name": ["Rahul", "Aman", "Priya"],
#     "Marks": [85, 90, 88],
#     "City": ["Delhi", "Chandigarh", "Mohali"]
# }
# df = pd.DataFrame(data)

# # Display the data
# print(df)

# # Line graph
# plt.plot(df["Name"], df["Marks"], marker="o")
# plt.title("Student Marks")
# plt.xlabel("Student Name")
# plt.ylabel("Marks")
# plt.show()


import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame
data = {
    "Name": ["Rahul", "Aman", "Priya"],
    "Marks": [85, 90, 88],
    "City": ["Delhi", "Chandigarh", "Mohali"]
}
df = pd.DataFrame(data)

# Display the data
print(df)

# Pie chart
plt.pie(df["Marks"], labels=df["Name"], autopct="%1.1f%%", startangle=90)
plt.title("Student Marks Distribution")
plt.axis("equal")  # Ensures the pie is drawn as a circle, not an oval
plt.show()