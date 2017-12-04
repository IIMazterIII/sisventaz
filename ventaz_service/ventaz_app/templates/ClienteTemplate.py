<h1>Welcome to Clinica</h1>
<form method="POST" action="">{% csrf_token %}
{{ var_form.as_p}}
<input type='submit' value='Registrar' />
</form>