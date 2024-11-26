import json

def convert_target_to_is_human(input_file, output_file):
    """
    Convierte un archivo JSON línea por línea, cambiando 'target' a 'is_human'.
    
    :param input_file: Ruta al archivo de entrada con formato 'target'.
    :param output_file: Ruta al archivo de salida con formato 'is_human'.
    """
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            data = json.loads(line.strip())
            
            if 'target' in data:
                data['is_human'] = 0.0 if data['target'][0] == 1 else 1.0
                del data['target']  
            
            outfile.write(json.dumps(data) + '\n')

# Uso del script
input_file = r'C:\Users\aleja\Documents\github\NLP\data\benchmarking\targets.jsonl'  
output_file = r'C:\Users\aleja\Documents\github\NLP\data\benchmarking\targets_converted.jsonl'  
convert_target_to_is_human(input_file, output_file)
