
import json 
import os 
import re 
from  web_scarping import save_json

def clean_data(path):
    try:
        if not os.path.exists(path):
            raise FileNotFoundError("File doesn't exist.")

        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

        cleaned_data = []

        for i in range(len(data)):

            page_data = {
                "page": data[i]["page"],
                "content": {}
            }

            for key, content in data[i]["page_content"].items():

                if isinstance(content, list):

                    lst = []

                    for obj in content:

                        for k, value in obj.items():

                            if isinstance(value, str):
                                temp = re.sub(r"\n+", " ", value)
                                temp = re.sub(r"\s+", " ", temp).strip()
                            else:
                                temp = value

                            lst.append({k: temp})

                    page_data["content"][key] = lst

                elif isinstance(content, str):

                    temp = re.sub(r"\n+", " ", content)
                    temp = re.sub(r"\s+", " ", temp).strip()

                    page_data["content"][key] = temp

                else:
                    page_data["content"][key] = content

            cleaned_data.append(page_data)

        print(cleaned_data)

        return cleaned_data

    except FileNotFoundError as e:
        print(e)

    except json.JSONDecodeError as e:
        print(f"Invalid JSON file: {e}")

    except Exception as e:
        print(f"Error: {e}")


data = clean_data("./day_7/json_data/data.json")

save_json(data,"./day_7/json_data/cleaned_data.json")



