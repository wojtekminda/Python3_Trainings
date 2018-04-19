'''
A user wants to access a Perforce branch.
To do that, he/she has to fill out a form and file a request.
Write a script which asks the user to provide some personal and technical data.
After the user enters all the data, the script echoes it back as a summary of the request.
'''

print("BRANCH ACCESS REQUEST FORM")

print("\nPERSONAL DATA")
first_name = input("First name: ")
last_name = input("Last name: ")
RnD = input("R&D: ")
team = input("Team: ")

print("\nBRANCH INFO")
server_port = input("Server port: ")
branch = input("Branch: ")
access_type = input("Access type (list|read|write): ")

print("\n-------")
print("REQUEST")
print("User", first_name, last_name, "from", team, "team of", RnD, "requests", access_type, "access to", branch, "branch of", server_port, "Perforce server.")
