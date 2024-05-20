import datetime

def should_i_respond(user_message, user_name):
    if user_message.lower() == "time" or user_message.lower() in ["pst", "est", "utc", "cst", "mst", "mexico", "gmt", "cest", "art", "jst", "aedt", "nzst", "hst"]:
        return True
    else:
        return False

def respond(user_message, user_name):
    if user_message.lower() == "time":
        return "Please select a time zone: PST (Pacific), EST (Eastern), UTC (Universal Coordinated), CST (Central), MST (Mountain), Mexico, GMT (Greenwich Mean), CEST (Central European), ART (Argentina), JST (Japan Standard), AEDT (Australian Eastern), NZST (New Zealand Standard), HST (Hawaii-Aleutian)"
    elif user_message.lower() == "pst":
        current_time = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-8))).strftime("%H:%M")
        return f"The current time in PST (Pacific) is {current_time}"
    elif user_message.lower() == "est":
        current_time = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-5))).strftime("%H:%M")
        return f"The current time in EST (Eastern) is {current_time}"
    elif user_message.lower() == "utc":
        current_time = datetime.datetime.now(datetime.timezone.utc).strftime("%H:%M")
        return f"The current time in UTC (Universal Coordinated) is {current_time}"
    elif user_message.lower() == "cst":
        current_time = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-6))).strftime("%H:%M")
        return f"The current time in CST (Central) is {current_time}"
    elif user_message.lower() == "mst":
        current_time = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-7))).strftime("%H:%M")
        return f"The current time in MST (Mountain) is {current_time}"
    elif user_message.lower() == "gmt":
        current_time = datetime.datetime.now(datetime.timezone.utc).strftime("%H:%M")
        return f"The current time in GMT (Greenwich Mean) is {current_time}"
    elif user_message.lower() == "cest":
        current_time = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=2))).strftime("%H:%M")
        return f"The current time in CEST (Central European) is {current_time}"
    elif user_message.lower() == "art":
        current_time = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-3))).strftime("%H:%M")
        return f"The current time in ART (Argentina) is {current_time}"
    elif user_message.lower() == "jst":
        current_time = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9))).strftime("%H:%M")
        return f"The current time in JST (Japan Standard) is {current_time}"
    elif user_message.lower() == "aedt":
        current_time = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=11))).strftime("%H:%M")
        return f"The current time in AEDT (Australian Eastern) is {current_time}"
    elif user_message.lower() == "nzst":
        current_time = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=12))).strftime("%H:%M")
        return f"The current time in NZST (New Zealand Standard) is {current_time}"
    elif user_message.lower() == "hst":
        current_time = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-10))).strftime("%H:%M")
        return f"The current time in HST (Hawaii-Aleutian) is {current_time}"