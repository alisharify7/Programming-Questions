1 -می خواهیم برنامه ای برای تشخیص گذرواژه به شکل زیر طراحی کنیم:
ابتدا کاربر باید گذرواژه مورد نظر را نویسه به نویسه در آرایه password وارد و کد اسکی متناظر با هر نویسه را
در آرایه code نگهداری کند.گذرواژه می تواند بین 8 تا 12 نویسه وفقط شامل حروف و اعداد باشد. تعداد نویسه
های گذرواژه را کاربرمشخص می کند. سپس آرایه code را به ترتیب نزولی مرتب کند.
اگر مجموع عناصر مضرب 5 آرایه code از مجموع عناصر اول –وسط وآخر کمتر باشد آنگاه پیام
“Password Good "داده شود و اگر بیشتر باشد پیام "Password Bad "داده شود در غیراینصورت برنامه
بتواند به دنبال یک نویسه دلخواه در آرایه password بگردد و تمام اندیس های پیدا شدن آنرا نمایش دهد.
در آخر گذرواژه با رنگ آبی روی سفید نمایش داده شود .

منبع : لیگ برنامه نویسی هنرجویان رشته شبه و نرم افزار استان البرز 

-------------
write a Program that take a password from user 
length of password must between 8 to 12 character
store each character of user input in a password list array []
then store each character ascii code in code list array []
password should be combination of Number or character
