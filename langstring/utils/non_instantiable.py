class NonInstantiable(type):
    """A metaclass that prevents the instantiation of any class that uses it.

    When a class is defined with NonInstantiable as its metaclass, any attempt to instantiate that class will result
    in a TypeError. This is useful for creating classes that are meant to be used as namespaces or containers for
    static methods and class variables, without the intention of creating instances.

    Methods:
        __call__: Overrides the default call behavior to prevent instantiation.
    """

    def __call__(cls) -> None:
        """Override the default call behavior to prevent instantiation of the class.

        When this method is called, it raises a TypeError, effectively preventing the creation of an instance of the
        class that uses NonInstantiable as its metaclass.

        :raises TypeError: Always, to indicate that the class cannot be instantiated.
        """
        raise TypeError(f"{cls.__name__} class cannot be instantiated.")
