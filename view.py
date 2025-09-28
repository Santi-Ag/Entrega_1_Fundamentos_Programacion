file_path = "names_report.jsonl"

with open(file_path, 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        if i < 5:  # Muestra los primeros 5 registros
            # Aquí la línea se imprime tal cual, como cadena de texto
            print(line.strip())  # strip() quita saltos de línea extra
        else:
            break