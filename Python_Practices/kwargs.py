import random
# Variable Length Arguments **kwargs (keywords Arguments)
def time_activity(*args, **kwargs):
    """
        Input : Multiple values for minutes, key=value pair activity
        Output: Return sum of minutes + random minute spect on a random
    """
    print(args)
    print(kwargs)
    min = sum(args) + random.randint(0, 60)
    print(min)
    choice = random.choice(list(kwargs.keys()))
    print(choice)
    print(f"You have to spend {min} for {kwargs[choice]}")


time_activity(
        10,
              20,
              10,
              hobby="Dance",
              sport="Boxing",
              fun="Driving",
              work="DevOps"
)