from flask import Flask, render_template_string

app = Flask(__name__)

# HTML-код вашей страницы
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Моя первая страница</title>
</head>
<body>
    <h1>Привет, мир!</h1>
    <p>Это моя первая HTML-страница.</p>
</body>
</html>
"""

@app.route('/')
def home():
    # Рендерим HTML-страницу
    return render_template_string(html_content)

if __name__ == '__main__':
    # Запускаем сервер на локальном хосте
    app.run(debug=True)
