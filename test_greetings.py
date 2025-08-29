```python
def greet(name):
    """Greets the person passed in as a parameter."""

    print(f"Hello, {name}!")


def test_greet():
    assert greet("World") is None  # Check that the function doesn't return anything
    assert greet("Universe") is None
