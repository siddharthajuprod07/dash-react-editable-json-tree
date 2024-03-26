import dash_react_editable_json_tree
from dash import Dash, callback, html, Input, Output, State

app = Dash(__name__)

data_json= {"menu": {
  "id": "file",
  "value": "File",
  "popup": {
    "menuitem": [
      {"value": "New", "onclick": "CreateNewDoc()"},
      {"value": "Open", "onclick": "OpenDoc()"},
      {"value": "Close", "onclick": "CloseDoc()"}
    ]
  }
}}

app.layout = html.Div([
    dash_react_editable_json_tree.DashReactEditableJsonTree(
        id='input',
        data=data_json
    ),
    html.Div(id='output'),
    html.Button('Submit', id='submit-val', n_clicks=0),
])


@callback(Output('output', 'children'), Input('submit-val', 'n_clicks'),State('input','updatedData'),State('input','data'))
def display_output(n,value,initial_data):
    print("callback fired")
    return 'You have entered {}'.format(value)


if __name__ == '__main__':
    app.run_server(debug=True)
