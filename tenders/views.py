from django.http import HttpResponse


def index(request):
    return HttpResponse(""" <!DOCTYPE html>
<html>
<head>
<title>Tenders</title>
</head>
<body>

<h1>Public tenders map</h1>
<p>This site displays map of contractors and principals connected by executed contracts.</p>

</body>
</html> """)

