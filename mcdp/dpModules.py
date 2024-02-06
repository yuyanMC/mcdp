from .dpTypes import dpString
class Functions:
    class Command:
        def say(message:dpString=dpString("")):
            return f"say {message.value}"