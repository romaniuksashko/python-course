# Завдання 4, Романюк, група ІТ-31

a = 12;
b = 5;
c = len("Romaniuk");

is_last_name_between_month_and_day = b <= c <= a;
is_day_bigger_than_month = a > b;
is_month_unequivalent_to_day = b != a;

is_last_name_equivalent_to_month = c == b;
is_month_bigger_or_equivalent_to_day = b >= a;
is_last_name_lesser_than_month = c < b;

print(f"b <= c <= a: {is_last_name_between_month_and_day}, {type(is_last_name_between_month_and_day)}");
print(f"a > b: {is_day_bigger_than_month}, {type(is_day_bigger_than_month)}");
print(f"b != a: {is_month_unequivalent_to_day}, {type(is_month_unequivalent_to_day)}");
print(f"c == b: {is_last_name_equivalent_to_month}, {type(is_last_name_equivalent_to_month)}");
print(f"b >= a: {is_month_bigger_or_equivalent_to_day}, {type(is_month_bigger_or_equivalent_to_day)}");
print(f"c < b: {is_last_name_lesser_than_month}, {type(is_last_name_lesser_than_month)}");