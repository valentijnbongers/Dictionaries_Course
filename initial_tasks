top_cs_universities = {
    "California Institute of Technology (Caltech)": ("Pasadena", "USA"),
    "Carnegie Mellon University": ("Pittsburgh", "USA"),
    "City University of Hong Kong": ("Hong Kong", "Hong Kong SAR"),
    "Columbia University": ("New York", "USA"),
    "Cornell University": ("Ithaca", "USA"),
    "EPFL (Ecole Polytechnique Fédérale de Lausanne)": ("Lausanne", "Switzerland"),
    "ETH Zurich - Swiss Federal Institute of Technology": ("Zurich", "Switzerland"),
    "Fudan University": ("Shanghai", "China"),
    "Georgia Institute of Technology": ("Atlanta", "USA"),
    "Harvard University": ("Cambridge", "USA"),
    "Imperial College London": ("London", "UK"),
    "KAIST - Korea Advanced Institute of Science & Technology": ("Daejeon", "South Korea"),
    "Lomonosov Moscow State University": ("Moscow", "Russia"),
    "Massachusetts Institute of Technology (MIT)": ("Cambridge", "USA"),
    "McGill University": ("Montreal", "Canada"),
    "National Taiwan University (NTU)": ("Taipei", "Taiwan"),
    "National University of Singapore (NUS)": ("Singapore", "Singapore"),
    "Nanyang Technological University, Singapore (NTU)": ("Singapore", "Singapore"),
    "New York University (NYU)": ("New York", "USA"),
    "Peking University": ("Beijing", "China"),
    "Pohang University of Science and Technology (POSTECH)": ("Pohang", "South Korea"),
    "Princeton University": ("Princeton", "USA"),
    "Stanford University": ("Stanford", "USA"),
    "Technical University of Munich": ("Munich", "Germany"),
    "The Hong Kong University of Science and Technology": ("Hong Kong", "Hong Kong SAR"),
    "The University of Hong Kong": ("Hong Kong", "Hong Kong SAR"),
    "The University of Melbourne": ("Melbourne", "Australia"),
    "Tsinghua University": ("Beijing", "China"),
    "University College London (UCL)": ("London", "UK"),
    "University of British Columbia": ("Vancouver", "Canada"),
    "University of California, Berkeley (UCB)": ("Berkeley", "USA"),
    "University of California, Los Angeles (UCLA)": ("Los Angeles", "USA"),
    "University of California, San Diego (UCSD)": ("San Diego", "USA"),
    "University of California, Santa Barbara (UCSB)": ("Santa Barbara", "USA"),
    "University of Cambridge": ("Cambridge", "UK"),
    "University of Chicago": ("Chicago", "USA"),
    "University of Edinburgh": ("Edinburgh", "UK"),
    "University of Illinois at Urbana-Champaign": ("Champaign", "USA"),
    "University of Maryland, College Park": ("College Park", "USA"),
    "University of Michigan-Ann Arbor": ("Ann Arbor", "USA"),
    "University of Oxford": ("Oxford", "UK"),
    "University of Pennsylvania": ("Philadelphia", "USA"),
    "University of Queensland": ("Brisbane", "Australia"),
    "University of Southern California": ("Los Angeles", "USA"),
    "University of Sydney": ("Sydney", "Australia"),
    "University of Texas at Austin": ("Austin", "USA"),
    "University of Toronto": ("Toronto", "Canada"),
    "University of Tokyo": ("Tokyo", "Japan"),
    "University of Washington": ("Seattle", "USA"),
    "University of Warwick": ("Coventry", "UK"),
    "University of Wisconsin-Madison": ("Madison", "USA")
}

# Task 1: Accessing Values
print("Task 1")
print(top_cs_universities["Stanford University"])
print(top_cs_universities["University of Oxford"])

# Task 2: Adding New Entries
print("Task 2")
print(top_cs_universities)

# Task 3: Modifying Values
print("Task 3")
top_cs_universities["University of Cambridge"] = ("Cambridge, England", "UK")
print(top_cs_universities)
# Task 4: Removing Entries
print("Task 4")
top_cs_universities.pop("Harvard University")
print(top_cs_universities)

# Task 5: Looping Through the Dictionary
print("Task 5")
for key in top_cs_universities:
    print(f"{key} is located in {top_cs_universities[key][0]}, {top_cs_universities[key][1]}")

# Task 6: Dictionary Methods
print("Task 6")
print(dict.keys(top_cs_universities))
print(dict.values(top_cs_universities))
print(dict.items(top_cs_universities))

# Task 7: Using get() Method
print("Task 7")
print(top_cs_universities.get("University of Tokyo"))
print(top_cs_universities.get("University of Delft", "Not Found"))
# Task 8: Updating Dictionary with update()
print("Task 8")
new_universities = {
    "University of California, Berkeley (UCB)": ("Berkeley", "USA"),
    "University of Illinois at Urbana-Champaign": ("Champaign", "USA")
}
top_cs_universities.update(new_universities)
print(top_cs_universities)


# Task 9: Dictionary Comprehension
print("Task 9")
UK_Universities = {}
for key in top_cs_universities:
    if top_cs_universities[key][1] == "UK":
        UK_Universities[key] = top_cs_universities[key]
print(UK_Universities)
