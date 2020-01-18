a = 0


def my_function():
    local = 10

    def func():
        nonlocal local
        local = 20

        def func1():
            nonlocal local
            local = 30

            def func2():
                global a
                a = 100

            func2()
        func1()
    func()
    return local

print(a)
print(a + my_function())
print(a)
