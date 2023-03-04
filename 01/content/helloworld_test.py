"""Testing Module for Learning program"""
import helloworld

def test_main(capfd):
    """This tests that the main function returns Hello World"""
    helloworld.helloworld()
    out, _ = capfd.readouterr()
    assert out == "Hello World\n"
