def test():
    from ...openmacro import computer
    code = "extensions.browser.search('externalities in economics', n=1)"
    results = computer.run_python(code)
    
    print(results)
    
test()