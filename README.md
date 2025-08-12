# Translate REST API

This is a Flask-based REST API for translating text using the Argos Translate library.

## Usage

Send a POST request to the `/translate` endpoint with the following JSON payload:

```
{
    "text": "your text here",
    "from_code": "source_language_code",
    "to_code": "target_language_code"
}
```

Replace `source_language_code` and `target_language_code` with the appropriate language codes.

## Example

To translate "Hello, world!" from English (en) to Spanish (es):

```
curl -X POST http://localhost:5000/translate \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Hello, world!",
    "from_code": "en",
    "to_code": "es"
  }'
```

Response:
```json
{
  "translated_text": "¡Hola, mundo!"
}
```

## Error Handling

- Returns a 400 status code if `text`, `from_code`, or `to_code` is missing.
- Returns a 404 status code if the translation package for the specified languages is not found.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
