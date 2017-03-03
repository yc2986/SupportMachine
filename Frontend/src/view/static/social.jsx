import React from "react"

const cssSocial =
{
    "WebkitTransform": "scale(0.8)",
    "MozTransform": "scale(0.8)",
    "WebkitTransformDuration": "0.5s",
    "MozTransformDuration": "0.5s",
    "OTransformDuration": "0.5s",
};

const cssSocialOnHover =
{
    "WebkitTransform": "scale(1.1)",
    "MozTransform": "scale(1.1)",
    "OTransform": "scale(1.1)",
    "color": "#f39c12",
};

class Social extends React.Component
{
    constructor(props) {
        super(props);
        this.state = {
            hover: false
        }
    }

    render() {
        return(
            <a href={ this.props.href }>
                <i className = { "fa fa-3x ".concat(this.props.icon) } 
                   style     = { cssSocial } />
            </a>
        );
    }
}

export default Social;