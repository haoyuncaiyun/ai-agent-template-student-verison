from core.state import STATE

def set_age(age: int):
    STATE["age"] = age
    return f"Your age is: {age}"

def pulse_result(pulseResult: int):
    STATE["pulse_results"].append(pulseResult)

    if pulseResult < 60:
        status = "low"
    elif pulseResult <= 100:
        status = "healthy/stable"
    else:
        status = "too high"

    return f"Your pulse is {pulseResult}, you are currently {status}."

def conversation_note(note: str):
    STATE["conversations"].append(note)
    return "I remembered this conversation."