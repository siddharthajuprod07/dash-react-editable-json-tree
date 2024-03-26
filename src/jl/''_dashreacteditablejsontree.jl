# AUTO GENERATED FILE - DO NOT EDIT

export ''_dashreacteditablejsontree

"""
    ''_dashreacteditablejsontree(;kwargs...)

A DashReactEditableJsonTree component.
ExampleComponent is an example component.
It takes a property, `label`, and
displays it.
It renders an input with the property `value`
which is editable by the user.
Keyword arguments:
- `id` (String; optional): The ID used to identify this component in Dash callbacks.
- `data` (Dict | Array; optional): JSON data
- `readOnly` (Bool; optional): Whether the whole structure will be readonly
- `updatedData` (Dict | Array; optional): Updated JSON data
"""
function ''_dashreacteditablejsontree(; kwargs...)
        available_props = Symbol[:id, :data, :readOnly, :updatedData]
        wild_props = Symbol[]
        return Component("''_dashreacteditablejsontree", "DashReactEditableJsonTree", "dash_react_editable_json_tree", available_props, wild_props; kwargs...)
end

