


# dates are easily constructed and formatted

from datetime import date

now = date.today()

print(now)
# 2025-03-16


birthday = date(1909, 10, 26)
age = now - birthday

print(age.days)
# 42145