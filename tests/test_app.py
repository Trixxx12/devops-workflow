import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')
from app import greet_user

def test_greet_user():
    result = greet_user("Jessica")
    assert result == "Hello, Jessica"



def test_greet_user_different_name():
    result = greet_user("John")
    assert result == "Hello, John"
