<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html><head>
  <title></title>
</head><body>
{% extends "base.html" %}
{% block contenido %}
      
<p>Lista de platos </p>

      
<ul>

{% for plato in lista_platos %}
        <li> <a href="platos/%7B%7Bplato.id%7D%7D">{{plato.nombre}}</a>
        </li>
{% endfor %}
      
</ul>


{% endblock %}
</body>
</html>