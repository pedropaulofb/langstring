"""This module provides the NonInstantiable metaclass used to prevent instantiation of classes.

The `control` module is designed to house the NonInstantiable metaclass, which is a utility to create classes that
cannot be instantiated. This is particularly useful in scenarios where a class is meant to serve as a collection of
static methods or class-level attributes, and creating instances of such a class would be illogical or unnecessary.

Classes:
    NonInstantiable (type): A metaclass to create non-instantiable classes.

Example:
    class MyClass(metaclass=NonInstantiable):
        # MyClass definition

    # Attempting to instantiate MyClass will raise a TypeError
    instance = MyClass()  # Raises TypeError
"""


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
