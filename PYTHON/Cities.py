polluted = {
    "Begusarai",
    "Guwahati",
    "Delhi",
    "Mullanpur",
    "Noida",
    "Greater Noida",
    "Hyderabad",
    "Meerut",
    "Ahmedabad",
    "Rohtak"
}
populated = {
    "Delhi",
    "Mumbai",
    "Kolkata",
    "Bengaluru",
    "Chennai",
    "Hyderabad",
    "Ahmedabad",
    "Surat",
    "Pune",
    "Jaipur"
}

print(f"Polluted but not populated: \n{polluted-populated} \n")
print(f"Populated but not polluted: \n{populated-polluted} \n")
print(f"Cities both Polluted and populated: \n{polluted.intersection(populated)} \n")
print(f"Cities either Populated or Polluted: \n{populated^polluted} \n")