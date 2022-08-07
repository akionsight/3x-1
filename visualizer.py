from matplotlib import pyplot as plt
import math


def three_x_plus_one(num):

    steps = [num]

    while (num > 1):

        if num % 2 == 0:
            num = num / 2
            steps.append(num)
            continue

        else:
            num = 3 * num + 1
            steps.append(num)
            continue
    
    return steps

## change the arguments of this function call below to the number you want to visualize
steps = three_x_plus_one(7225)

print(steps)

plt.plot(steps, color="magenta")
plt.plot()


plt.xlabel(f"Number of Steps: {len(steps)}")
plt.ylabel(f"Values Achieved: {max(steps)}")

plt.show()
