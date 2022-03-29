# **_Regular expression._**


![image](https://user-images.githubusercontent.com/85587286/160545403-aacdeae1-0ca5-43e3-95b4-5728ef9af4f3.png)

## **_Resources:_**

### **_Read or watch:_**


>> * [Ruby](https://rubular.com/)
>> * [PHP/Javascript/Python](https://regex101.com/)
>> * [Regular expressions - basics](https://www.slideshare.net/neha_jain/introducing-regular-expressions)
>> * [Regular expressions - advanced](https://www.slideshare.net/neha_jain/advanced-regular-expressions-80296518)
>> * [Rubular is your best friend](https://rubular.com/)
>> * [Use a regular expression against a problem: now you have 2 problems](https://blog.codinghorror.com/regular-expressions-now-you-have-two-problems/)
>> * [Learn Regular Expressions with simple, interactive exercises](https://regexone.com/)


## **_Built with:_** 🛠️

>> * Ubuntu 20.4 LTS
>> 
>> * Emacs editor


## **_Background Context:_**

 	

~~~~

For this project, I have to build your regular expression using Oniguruma, a regular expression library that which is used by Ruby by default. Note that other regular expression libraries sometimes have different properties.

Because the focus of this exercise is to play with regular expressions (regex), here is the Ruby code that you should use, just replace the regexp part, meaning the code in between the //:

quinto@ubuntu$ cat example.rb
#!/usr/bin/env ruby
puts ARGV[0].scan(/127.0.0.[0-9]/).join
quinto@ubuntu$
quinto@ubuntu$ ./example.rb 127.0.0.2
127.0.0.2
quinto@ubuntu$ ./example.rb 127.0.0.1
127.0.0.1
quinto@ubuntu$ ./example.rb 127.0.0.a
 	

~~~~
