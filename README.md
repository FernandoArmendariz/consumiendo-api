# Consumiendo API de Rick and Morty

El objetivo principal de este ejercicio es practicar el consumo de una API externa, transformar la información recibida y devolverla en un formato adecuado (JSON). En este caso, consumirás la API pública de Rick and Morty y devolverás el nombre y el estado de un personaje, basándote en un número proporcionado en el cuerpo de la petición HTTP.

## Estructura del Proyecto

consumiendo-api/

- app.py
- tests/
  - test_character.py
- requirements.txt
- README.md

## Requisitos

- Flask
- Requests

## Instalación

1. Clona este repositorio:

   ```sh
   git clone https://git.utec.edu.uy/fernando.armendariz/consumiendo-api.git
   cd consumiendo-api
   ```
2. Crea un entorno virtual y actívalo:

   ```sh
   python -m venv .venv
   .venv\Scripts\activate.bat  # En Windows
   # source venv/bin/activate  # En macOS/Linux
   ```
3. Instala las dependencias:

   ```sh
   pip install -r requirements.txt
   ```

## Uso

1. Ejecuta la aplicación Flask:

   ```sh
   python app.py
   ```
2. Envía una solicitud POST a `http://127.0.0.1:5000/character` con el encabezado `Content-Type: application/json` y un cuerpo JSON que contenga `character_id`. Por ejemplo:

   ```json
   {
       "character_id": 1
   }
   ```

### Ejemplo de solicitud con cURL

```sh
curl -X POST http://127.0.0.1:5000/character -H "Content-Type: application/json" -d '{"character_id": 1}'
```

### Ejemplo de solicitud con Postman

URL: {"http://127.0.0.1:5000/character"}
Método: POST
Encabezado: {"Content-Type: application/json"}
Cuerpo (Body): Selecciona {"raw"} y ["JSON"] y envía un JSON válido, por ejemplo:
Pruebas
Para ejecutar las pruebas, usa el siguiente comando:

```sh
{
    "character_id": 1
}
```

## Pruebas

Para ejecutar las pruebas, usa el siguiente comando:

```sh
python -m unittest discover -s ./tests -p "test_*.py"
```

## Licencia

Sin definir
