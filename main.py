import smtplib
import datetime as dt
import random

my_email = "active181105@gmail.com"
password = "bdakhhqileoybvck"

day = dt.datetime.now()
week_day = day.weekday()
if week_day == 5:
    print(week_day)
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        random_quote = random.choice(all_quotes)
    print(random_quote)
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email , password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="darkish@myyahoo.com",
            msg=f"Subject:Monday Motivation\n\n{random_quote}"
            )