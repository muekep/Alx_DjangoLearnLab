<!-- book_form.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ action }} Book</title>
</head>
<body>
    <h1>{{ action }} Book</h1>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">{{ action }} Book</button>
    </form>
    <p><a href="{% url 'relationship_app:book_list' %}">Back to Book List</a></p>
</body>
</html>
