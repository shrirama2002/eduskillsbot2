from rasa_sdk.types import DomainDict
from inspect import getmembers, isfunction
print(getmembers(DomainDict,isfunction))
