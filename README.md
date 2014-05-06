# Carpentry

Lean models for Python.

This is an implementation of "models" similar to those you see in most
ORMs / forms definition systems, but with the main goal of keeping
things as simple as possible.

No metaclasses or descriptors are involved; no hackish code messing up
with standard Python objects functionality either.


## Example model definition

```python
from carpentry.base import BaseObject
from carpentry.common_fields import StringField, IntegerField

class MyModel(BaseObject):
    first_name = StringField()
	last_name = StringField()
	age = IntegerField()
```

Then, you can use it like this:

```python
>>> obj = MyModel()

>>> obj.first_name = 'Hello'

>>> obj.age = 20

>>> obj.age = 'invalid'
TypeError: ...
```

And prepare it for serialization (via json, msgpack, ..):

```python
>>> obj.serialize()
{
    'first_name': 'Hello',
	'last_name': '',
	'age': 20,
}
```
