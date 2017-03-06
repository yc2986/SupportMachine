import React from "react"

const cssSocial =
{
    "WebkitTransform": "scale(0.8)",
    "MozTransform": "scale(0.8)",
    "OTransform": "scale(0.8)",
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
        this.hoverHandler = this.hoverHandler.bind(this)
        this.state = {
            hover: false,
        }
    }

    getInitialState() {
        return {
            hover: false,
        };
    }

    hoverHandler() {
        this.setState({
            hover: !this.state.hover,
        });
    }

    render() {
        let iconStyle = (this.state.hover) ? cssSocialOnHover : cssSocial;
        return(
            <a href={ this.props.href } onMouseEnter={ this.hoverHandler } onMouseLeave={ this.hoverHandler }>
                <i className = { "fa fa-3x ".concat(this.props.icon) } 
                   style     = { iconStyle } />
            </a>
        );
    }
}

export default Social;