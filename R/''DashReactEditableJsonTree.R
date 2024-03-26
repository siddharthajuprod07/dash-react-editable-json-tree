# AUTO GENERATED FILE - DO NOT EDIT

#' @export
''DashReactEditableJsonTree <- function(id=NULL, data=NULL, readOnly=NULL, updatedData=NULL) {
    
    props <- list(id=id, data=data, readOnly=readOnly, updatedData=updatedData)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'DashReactEditableJsonTree',
        namespace = 'dash_react_editable_json_tree',
        propNames = c('id', 'data', 'readOnly', 'updatedData'),
        package = 'dashReactEditableJsonTree'
        )

    structure(component, class = c('dash_component', 'list'))
}
