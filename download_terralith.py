import requests
import zipfile
import io

print("Downloading pack... ", end="")
terralith_pack = requests.post("https://seedfix.stardustlabs.net/", data={"seed": ""}).content
print("done!")

with zipfile.ZipFile(io.BytesIO(terralith_pack), "r") as outfile:
    outfile.extractall("terralith")

with open("terralith/data/minecraft/overworld.json", "r") as infile:
    print(infile.read())