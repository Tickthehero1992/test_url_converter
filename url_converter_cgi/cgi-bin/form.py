import cgi
import html
from test import url_to_out
form=cgi.FieldStorage()
url_input = form.getfirst("Input_url",'no data')#получение значения из index.html
url_out="domen://test_domen/" #сокращенная ссылка

url_converted=url_to_out(url_input)#преобразование ссылки
if(url_converted!=url_input):
    url_out+=url_converted
else:
    url_out=url_converted
#формирование страницы для сервера
web="""
<!DOCTYPE html>
<html lang="en">
<style type="text/css">
.button2
{
  background-color: #ff0ff0;
  border: none;
  color: black;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;
  line-height:10px;
  border-radius: 10px;
  vertical-align: top;
  border:solid black 1px;
  line-height:13px;
  font-size: 13px;

}
.url2
{
  background-color: #ffffff;
  border: none;
  color: black;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;
  line-height:10px;
  vertical-align: top;
  border:solid black 1px;
  line-height:13px;
  font-size: 13px;

}
</style>

<head>
    <meta charset="UTF-8">
    <title>Test URL_convert</title>
</head>
<body>
<form action="/cgi-bin/form.py">
    <h1>"""
web+="""
        <input class="url2" type="url" name="Input_url" onclick="Func_zero(this)" value="""+url_input
web+=""">"""

web+="""
        <input class="button2" type="submit" value="Convert" > 
        </form>"""
web+="<h2>"

web+= "<a href="+ url_input+">" + url_out+"</a>"
        
web+="""  </h2>

</body>
<script>

function Func_zero(elem)
{
if(elem.value=="Enter URL")
    {
    elem.value="";
    }
}

function Func_size(elem)
{
elem.size = 500;
}
</script>

"""
print(web)