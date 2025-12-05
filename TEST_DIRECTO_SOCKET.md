# 🔍 TEST DIRECTO DEL SOCKET

El servidor está corriendo pero no responde. Vamos a diagnosticar directamente en FreeCAD.

## PASO 1: Verificar estado del servidor en FreeCAD

**Copia y pega esto en la Consola de Python de FreeCAD:**

```python
# Verificar servidor
if hasattr(FreeCAD, '__ai_socket_server'):
    srv = FreeCAD.__ai_socket_server
    print(f"Servidor existe: True")
    print(f"Puerto: {srv.port}")
    print(f"Host: {srv.host}")
    print(f"Is running: {srv.is_running}")
    print(f"Socket: {srv.server_socket}")
    print(f"Conexiones activas: {len(srv.client_connections)}")
else:
    print("Servidor NO existe")
```

## PASO 2: Test manual con socket desde FreeCAD

**Ejecuta esto EN FREECAD para crear un cliente de prueba:**

```python
import socket
import json

# Crear cliente
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.settimeout(5)

try:
    # Conectar
    print("Conectando a localhost:23456...")
    client.connect(('localhost', 23456))
    print("✓ Conectado")

    # Enviar mensaje
    message = {
        "tool": "execute_python",
        "args": {"code": "result = 'Hello from test!'"}
    }

    data = json.dumps(message).encode('utf-8') + b'\n'
    print(f"Enviando: {message}")
    client.sendall(data)
    print("✓ Mensaje enviado")

    # Esperar respuesta
    print("Esperando respuesta...")
    response = client.recv(4096)
    print(f"✓ Respuesta recibida: {response.decode('utf-8')}")

except Exception as e:
    print(f"✗ Error: {e}")
    import traceback
    traceback.print_exc()
finally:
    client.close()
```

## QUÉ ESPERAR:

### Si funciona:
```
Conectando a localhost:23456...
✓ Conectado
Enviando: {'tool': 'execute_python', 'args': {'code': "result = 'Hello from test!'"}}
✓ Mensaje enviado
Esperando respuesta...
✓ Respuesta recibida: {"success": true, "result": "Hello from test!"}
```

### Si NO funciona:
Veremos exactamente dónde falla y podremos diagnosticar.

---

## EJECUTA ESTOS DOS TESTS EN FREECAD Y DIME QUÉ VES
