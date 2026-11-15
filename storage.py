import json 
from pathlib import Path

file_path = Path("data.json")

def load_trans():
    
    if not file_path.exists():
        return []
    
    with open(file_path,'r',encoding='utf-8') as file:
       return json.load(file)
    

def save_trans(transactions):

    with open(file_path,'w',encoding='utf-8') as file:
        json.dump(transactions,file,indent=4)





