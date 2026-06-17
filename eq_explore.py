from pathlib import Path
import json

# 1
path = Path('Earthquakes_json/all_day.geojson.json')

# 2 
contents = path.read_text()

# 3 
all_eq_data = json.loads(contents)

# Indicar la ruta para guardar el archivo
path = Path('Earthquakes_json/readeble_data_json.json')

# Hacer legible el archivo json; indent: para sangrar elementos
readable_contents = json.dumps(all_eq_data, indent=4)

# 5
path.write_text(readable_contents)
