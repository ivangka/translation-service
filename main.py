from flask import Flask, request, jsonify
import argostranslate.package
import argostranslate.translate

app = Flask(__name__)

# Update the package index on application startup
argostranslate.package.update_package_index()
available_packages = argostranslate.package.get_available_packages()

# Function to install the translation package for the specified language codes
def install_translation_package(from_code, to_code):
    package_to_install = next(
        (pkg for pkg in available_packages if pkg.from_code == from_code and pkg.to_code == to_code),
        None
    )
    if package_to_install:
        argostranslate.package.install_from_path(package_to_install.download())
        return True
    return False

# Endpoint to translate text
@app.route('/translate', methods=['POST'])
def translate_text():
    data = request.get_json()
    text = data.get("text")
    from_code = data.get("from_code")
    to_code = data.get("to_code")

    # Check if text and language codes are provided
    if not text or not from_code or not to_code:
        return jsonify({"error": "Please provide 'text' and language codes 'from_code' and 'to_code'"}), 400

    # Install the required translation package if it's not installed
    if not install_translation_package(from_code, to_code):
        return jsonify({"error": f"Translation package from {from_code} to {to_code} not found"}), 404

    # Perform the translation
    translated_text = argostranslate.translate.translate(text, from_code, to_code)
    return jsonify({"translated_text": translated_text})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
