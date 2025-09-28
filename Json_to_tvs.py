import json   # Import the JSON library to parse JSONL lines

file_path = "names_report.jsonl"   # Input JSONL file
output_path = "names_report_table3.tsv"  # Output TSV file

data = []  # List to store extracted records

# Read the JSONL file line by line
with open(file_path, 'r', encoding='utf-8') as f:
    for line in f:
        record = json.loads(line)   # Parse each line into a Python dictionary

        taxonomy = record.get("taxonomy", {})   # Access the "taxonomy" field
        taxId = taxonomy.get("taxId", "")       # Extract the taxId value
        rank = taxonomy.get("rank", "")         # Extract the rank value
        name = taxonomy.get("currentScientificName", {}).get("name", "")  # Extract the scientific name
        group = taxonomy.get("groupName", "")   # Extract the group name

        data.append([taxId, rank, name, group])  # Save the row into our list

# Write the TSV file
with open(output_path, "w", encoding="utf-8") as f_out:
    f_out.write("taxId\trank\tname\tgroupName\n")  # Write the header
    for row in data:
        f_out.write("\t".join(row) + "\n")        # Write each row separated by tabs

# Print the table to the console
print("taxId\trank\tname\tgroupName")   # Print the header
for row in data:
    print("\t".join(row))               # Print each row
