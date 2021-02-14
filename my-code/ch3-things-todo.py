#How many seconds are in an hour?
seconds_per_minute = 60
minutes_per_hour = 60

seconds_per_hour = seconds_per_minute * minutes_per_hour
print(seconds_per_hour)

hours_per_day = 24
total_seconds_per_day = seconds_per_hour * hours_per_day
print(total_seconds_per_day)

print("\n")

#/////Using floating-point / division
decimal_answer = total_seconds_per_day / seconds_per_hour
print(decimal_answer)

#/////Using integer // division
no_decimal_answer = total_seconds_per_day // seconds_per_hour
print(no_decimal_answer)



#///// My old code is  below

# #///// Redo ch3 Todo

# quick_total = 60 * 60
# print(quick_total)

# seconds_per_minute = 60
# seconds_per_hour = 60

# seconds_per_day = seconds_per_minute * seconds_per_hour
# print(seconds_per_day)

# total_one = seconds_per_day / seconds_per_hour
# print(total_one)

# total_two = seconds_per_day // seconds_per_hour
# print(total_two)