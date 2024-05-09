from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    """Test the function make_full_name verifing.
    Parameters: none
    Return: none
    """
    assert make_full_name("Guilherme", "Machado") == "Machado;Guilherme"

def test_extract_family_name():
    """Test the function make_full_name verifing.
    Parameters: none
    Return: none
    """
    assert extract_family_name("Machado; Guilherme") == "Machado"

def test_extract_given_name():
    """Test the function make_full_name verifing.
    Parameters: none
    Return: none
    """
        
    assert extract_given_name("Machado; Guilherme") == "Guilherme"

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])