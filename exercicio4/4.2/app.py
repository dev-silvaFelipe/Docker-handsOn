import redis


r = redis.Redis(host='meu-redis', port=6379, decode_responses=True)

r.set('mensagem', 'A comunicacao entre containers esta funcionando perfeitamente!')
valor = r.get('mensagem')

print(f"Resposta do Redis: {valor}")