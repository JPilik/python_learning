"""Testing Module for Learning program"""
import helloworld

def test_main(capfd):
    """Test the main function returns Hello World"""
    helloworld.helloworld()
    out, _ = capfd.readouterr()
    assert out == "Hello World\n"
