import requests 
base_url = 'https://jsonplaceholder.typicode.com/posts/1'

# PUT - Atualizar completamente
dados_atualizados = {
    'id' : 1,
    'title' : 'Título Atualizado',
    'body' : 'Novo conteúdo',
    'userId' : 1
} 

resp_put = requests.put(base_url, json = dados_atualizados)
print(f"PUT status: {resp_put.status_code}")

#PATCH - Atualizar parcialmente
resp_patch = requests.patch(base_url, json = {'title' : 'Apenas o título'})
print(f"PATCH status: {resp_patch.status_code}")

# DELETE - Remover
resp_delete = requests.delete(base_url)
print(f"DELETE status: {resp_delete.status_code}")