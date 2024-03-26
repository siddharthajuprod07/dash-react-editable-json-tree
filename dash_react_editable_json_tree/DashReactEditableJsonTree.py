# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DashReactEditableJsonTree(Component):
    """A DashReactEditableJsonTree component.
ExampleComponent is an example component.
It takes a property, `label`, and
displays it.
It renders an input with the property `value`
which is editable by the user.

Keyword arguments:

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- data (dict | list; optional):
    JSON data.

- readOnly (boolean; optional):
    Whether the whole structure will be readonly.

- updatedData (dict | list; optional):
    Updated JSON data."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_react_editable_json_tree'
    _type = 'DashReactEditableJsonTree'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, data=Component.UNDEFINED, updatedData=Component.UNDEFINED, readOnly=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'data', 'readOnly', 'updatedData']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'data', 'readOnly', 'updatedData']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(DashReactEditableJsonTree, self).__init__(**args)
