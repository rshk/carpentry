Usage
#####

Creating your models is pretty straight-forward: just inherit from
:py:class:`carpentry.base.BaseObject` and define some fields.


.. code-block:: python

    from carpentry import BaseObject, StringField, BoolField

    class User(BaseObject):
        first_name = StringField(required=True)
        last_name = StringField(required=True)
        email = StringField(required=True)
	is_administrator = BoolField(default=False)


Then you can start using it right away:

.. code-block:: python

    >>> user = User({'first_name': 'John', 'last_name': 'Doe'})
    >>> user.email = 'john.doe@example.com'


And now serialize it and get ready for (inserting in a database |
sending via an API | ...):

.. code-block:: python

    >>> obj.serialize()
    {
    'first_name': 'John',
    'last_name': 'Doe',
    'email': 'john.doe@example.com',
    'is_administrator': False,
    }


Also, fields provide basic validation, so if you try, for example, to:

.. code-block:: python

    >>> obj.is_administrator == 'FooBar'

You'll get a ``TypeError``.
