from stack_project import Node, Stack
import pytest

def test_print_Null(capfd):
    stack = Stack()
    print(stack)
    captured = capfd.readouterr()
    assert captured.out == "[]\n"

def test_print_single_item_list(capfd):
    stack = Stack()
    stack.Push(12)
    print(stack)
    captured = capfd.readouterr()
    assert captured.out == "[12]\n"

def test_print(capfd):
    stack = Stack()
    stack.Push(12)
    stack.Push(14)
    stack.Push(9)
    stack.Push(-5)
    print(stack)
    captured = capfd.readouterr()
    assert captured.out == "[12, 14, 9, -5]\n"

def test_pop(capfd):
    stack = Stack()
    stack.Push(12)
    stack.Push(14)
    stack.Push(9)
    stack.Push(-5)
    stack.Pop()
    stack.Pop()
    print(stack)
    captured = capfd.readouterr()
    assert captured.out == "[12, 14]\n"

def test_print_Null_after_Pop(capfd):
    stack = Stack()
    stack.Push(12)
    stack.Push(14)
    stack.Push(9)
    stack.Push(-5)
    stack.Pop()
    stack.Pop()
    stack.Pop()
    stack.Pop()
    print(stack)
    captured = capfd.readouterr()
    assert captured.out == "[]\n"

def test_error_Pop():
    with pytest.raises(IndexError) as e_info:
        stack = Stack()
        stack.Pop()

def test_isEmpty():
    stack = Stack()
    assert stack.isEmpty() == True

def test_isEmpty_2():
    stack = Stack()
    stack.Push(15)
    assert stack.isEmpty() == False

def test_isEmpty_3():
    stack = Stack()
    stack.Push(15)
    stack.Pop()
    assert stack.isEmpty() == True

def test_Size():
    stack = Stack()
    stack.Push(12)
    stack.Push(14)
    stack.Push(9)
    stack.Push(-5)
    stack.Pop()
    stack.Pop()
    assert stack.Size() == 2

def test_Top():
    stack = Stack()
    stack.Push(12)
    stack.Push(14)
    stack.Push(9)
    stack.Push(-5)
    stack.Pop()
    stack.Pop()
    assert stack.Top() == 14