
module DashReactEditableJsonTree
using Dash

const resources_path = realpath(joinpath( @__DIR__, "..", "deps"))
const version = "0.0.1"

include("jl/''_dashreacteditablejsontree.jl")

function __init__()
    DashBase.register_package(
        DashBase.ResourcePkg(
            "dash_react_editable_json_tree",
            resources_path,
            version = version,
            [
                DashBase.Resource(
    relative_package_path = "dash_react_editable_json_tree.min.js",
    external_url = nothing,
    dynamic = nothing,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "dash_react_editable_json_tree.min.js.map",
    external_url = nothing,
    dynamic = true,
    async = nothing,
    type = :js
)
            ]
        )

    )
end
end