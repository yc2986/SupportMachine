import React from "react"

const cssLink = 
{
    "WebkitTransitionDuration": "0.8s",
    "MozTransitionDuration": "0.8s",
    "OTransitionDuration": "0.8s",
    "color": "white",
    "fontSize": "18px",
    "lineHeight": "40px",
}

const cssLinkOnHover = 
{
    "color": "white",
    "lineHeight": "40px",
    "textDecoration": "none",
    "fontSize": "20px",
}

class DolbyFooterLink extends React.Component
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
        let linkStyle = (this.state.hover) ? cssLinkOnHover : cssLink;
        return(
            <a href         = { this.props.href } 
               onMouseEnter = { this.hoverHandler } 
               onMouseLeave = { this.hoverHandler }
               style        = { linkStyle }>
               { this.props.text }
            </a>
        );
    }
}

export default DolbyFooterLink;