#for i in [1,2, 3]:
#
#    print(i)
#    

"""Leer archivos """

#with open("/home/aeonics/Documentos/texto.txt","r") as file:
#    updates = file.read()
#updates = updates.split(",")
#print(updates)
#updates = " ".join(updates)
#with open("/home/aeonics/Documentos/texto.txt","w") as file:
#    file.write(updates)
#print(updates)

def update_file(import_file, remove_list):
  with open(import_file, "r") as file:
    ip_addresses = file.read()

  ip_addresses = ip_addresses.split()

  for element in ip_addresses:
    if element in remove_list:
      ip_addresses.remove(element)

  ip_addresses = " ".join(ip_addresses)       

  with open(import_file, "w") as file:
    file.write(ip_addresses)

update_file(import_file,remove_list)
with open(import_file, "r") as file:
  text = file.read()

print(text)