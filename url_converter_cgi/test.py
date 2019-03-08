
s="http://rambler.ru"
s1="https://www.programiz.com/python-programming/methods/built-in/hex"
s2="https://www.youtube.com/watch?v=5OosYmG6CtE&list=PLub2DgMClK1NhFClb38Rtk9-l1yZuvLT3&index=14"

def convert_url(entered_url): #функция получения байт строки
   text=b''
   for c in entered_url:
        b=c.encode('utf-8')
        text+=b
   return text

def filter(url): #фнкция поиска / для отсеивания прмых ссылок на сай
   i=0
   for c in url:
      if c=='/':
            i+=1
   return i

from Cryptodome.Cipher import DES

def pad(text):  #преобразование строки в байт код для алгоритма DES
   while len(text) % 8 != 0:
      text += b' '
   return text

key = b'ers3sswe' # ключ шифрования для алгоритма DES
des = DES.new(key, DES.MODE_ECB)
def  url_to_out(url): #функция сокращения ссылки
   if(filter(url)>2): # отфильтровываем ссылку имеющую менее трех знаков '/'
      text1= convert_url(url) # преобразуем полученную ссылку
      padded_text = pad(text1) # полученное значение преобразуем для обработки алгоритмом шифрования
      #encrypt
      encrypted_text = des.encrypt(padded_text) #шифрование
      #введем переменные для формирования ссылки
      out=0 #сумма остатков при делении на 16 всех байт шифрованного сообщения
      i=0 #подсчет байт шифрованного сообщения
      out2=0 #сумма всех байт шифрованного сообщения
      out3="" #конечная строка для формирования ссылки
      for c in encrypted_text:
         out3+=str(c)
         out+=c%16
         out2+=c
         i+=1

      part1=hex(out)[-1] # последние байты  полученных переменных
      part2=hex(out2)[-1]
      part3=hex(out+out2+i)[-1]
      hased =hex(hash(text1))[-1]#подсчет хэша и сохранение последнего байта
      symbl=chr(int(part1)+int(part2)+65)  #формирование символа в ASCII
      out3=part1
      out3+=part2+part3+symbl+hased
      return(out3)
   else:
      return (url)# если ссылка с двумя '/' то возвращаем пришедшее значение

#decrypt расшифровка ссылки
def decode(encrypted_text):
   data = des.decrypt(encrypted_text)
   print(data)