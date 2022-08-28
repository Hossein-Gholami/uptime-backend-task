# uptime-backend-task
#### A Python backend task defined by Uptime 
##### developed with django and drf

#### <div style="text-align: right; direction: rtl;"> مدل ER </div>

![Alt er](assets/models.svg?raw=true "ER")

#### <div style="text-align: right; direction: rtl;"> توضیحات </div>
<p style="text-align: right; direction: rtl;">
دو موجودیت اصلی راننده و ماموریت هاست. برای برآورده کردن مفروضات مطرح شده راهکار در این کد پیاده شده،
بدین صورت است که از جدول سفارش ها یک کلید خارجی در مدل راننده نگه داری میکنیم. در آن واحد این کلید خارجی به سفارشی ارجاع دارد که راننده در حال انجام است.
</p>

#### <div style="text-align: right; direction: rtl;"> فرآیند </div>
<p style="text-align: right; direction: rtl;">
<ul style="text-align: right; direction: rtl;">

<li>کاربرانی به عنوان راننده از قبل ثبت شده اند.</li>
<li>یک سفارش جدید ذخیره میشود.</li>
<li>این یک سیگنال میدهد که با توجه به آن محاسبات زیر انجام میشود.</li>
<li>راننده کاندید برای انجام سفارش را پیدا کرده؛</li>
<li>این سفارش به وی تخصیص داده میشود.</li>
<li>پس از تحویل سفارش، راننده مجدد به حالت آزاد در میاد.</li>

</ul>
</p>

#### <div style="text-align: right; direction: rtl;"> اجرا </div>
##### pip install
first clone the project
then `pipenv install` or `pip install -r requirements.txt`
cd to project folder
`python manage.py makemigrations && python manage.py migrate`
`python manage.py createsuperuser`
finally `python manage.py runserver`
##### docker
cd to project directory and
`docker-compose up`

#### <div style="text-align: right; direction: rtl;"> چند نکته </div>
<p style="text-align: right; direction: rtl;">
تا جاییکه مقدور بود سعی بر کم بودن تعداد مدلها بود. هرچند این نتیجه رو گرفتم که ممکنه اینگتریتی دیتا بیس به خطر بیفته و دقت بیشتری رو نیاز داره.
</p>
<p style="text-align: right; direction: rtl;">
فعلا و به اشتباه از CharField برای لوکیشن استفاده کردم. دلیلش هم اینه که در موقعیت فعلی اهمیتی نداشت.
</p>
<p style="text-align: right; direction: rtl;">
راه حل کاملتر سلری و چنلز رو هم نیاز داره. سلری برای اینکه هر چند ثانیه اطلاعات لوکیشن راننده ها گرفته بشه. و چنلز هم برای این که به محض تخصیص سفارشی به یک راننده، اطلاعات مربوطه برای اون راننده ارسال بشه یعنی یک حالت نوتیفیکیشن.
</p>
<p style="text-align: right; direction: rtl;">

</p>