# Question1:
# Use a dictionary to store information about a person you know. Store their first name, last name, age,
# and the city in which they live. You should have keys such as first_name, last_name, age, and city. Print
# each piece of information stored in your dictionary. Add a new key value pair about qualification then
# update the qualification value to high academic level then delete it.
stu_info = {
    "first_name":"Muhammad Hamza","last_name":"Muhammad Jawed","age":19,"city":"Karachi"}
stu_info ["qualification"]= "intermediate"
print(stu_info)
stu_info["qualification"]= "graduation"
print(stu_info)
del stu_info["qualification"]
print(stu_info)