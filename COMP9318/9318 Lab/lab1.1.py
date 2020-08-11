def nsqrt(x):  # do not change the heading of the function
    if (x < 0):
        return False
    if (x == 0):
        return 0
    if (x == 1):
        return 1
    if (x == 2):
        return 1

    left = 1;
    right = int(x / 2) + 1;  # the max root is not more than 2
    mid = int(left + (right - left) / 2);
    output = 1;
    while (left < right):
        if mid * mid == x:
            break
        elif mid * mid > x:
            right = mid - 1
            mid = int(left + (right - left) / 2)
        elif mid * mid < x:
            left += 1
            mid = int(left + (right - left) / 2)
    if (mid * mid > x):
        output = int(mid - 1);
    else:
        output = int(mid);
    return output


x = 99
a = nsqrt(x)
print("result", a)
