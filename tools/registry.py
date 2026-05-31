from tools.tools import *

TOOLS = {
    "set_age": set_age,
    "pulse_result": pulse_result,
    "conversation_note": conversation_note,
}

TOOL_DESCRIPTIONS = {
    "set_age": "Sets the age of the elderly user. args: age:int",
    "pulse_result": "Records pulse and tells if it is low, healthy/stable, or too high. args: pulseResult:int",
    "conversation_note": "Stores an important conversation note. args: note:str",
}


#DESCRIPTION AND NAME OF THE TOOL AND WHAT THE TOOL DOES, SO AI FIGURE OUT WHAT TOOL TO USE AND PICK IT