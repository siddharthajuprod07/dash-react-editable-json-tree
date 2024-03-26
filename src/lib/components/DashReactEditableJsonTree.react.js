import React, { useState } from 'react';
import PropTypes from 'prop-types';
import {
    JsonTree,
    ADD_DELTA_TYPE,
    REMOVE_DELTA_TYPE,
    UPDATE_DELTA_TYPE,
    DATA_TYPES,
    INPUT_USAGE_TYPES,
} from 'react-editable-json-tree'

/**
 * ExampleComponent is an example component.
 * It takes a property, `label`, and
 * displays it.
 * It renders an input with the property `value`
 * which is editable by the user.
 */
const DashReactEditableJsonTree = (props) => {
    const {id, data, setProps,updatedData, readOnly} = props;

    const setval = (currentval) => {
        setProps({
            updatedData: currentval,
        });
    };

    return (
        <div>
            <JsonTree data={data} onFullyUpdate={setval} readOnly={readOnly}/>
        </div>
    );
}

DashReactEditableJsonTree.defaultProps = {};

DashReactEditableJsonTree.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string,

    /**
     * JSON data
     */
    data: PropTypes.oneOfType([
        PropTypes.object.isRequired,
        PropTypes.array.isRequired
    ]),

    /**
     * Updated JSON data
     */
    updatedData: PropTypes.oneOfType([
        PropTypes.object.isRequired,
        PropTypes.array.isRequired
    ]),

    /**
     * Whether the whole structure will be readonly
     */
    readOnly: PropTypes.bool,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};

export default DashReactEditableJsonTree;
