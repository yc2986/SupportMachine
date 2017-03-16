import React from "react"
import DolbyVideoJonbtron from "./dolbyvideojonbtron.jsx"

const cssCarouselItem = 
{
    "position": "relative",
    "background": "radial-gradient(#303030 1%, black 99%)",
    "width": "50%",
    "transition": "all 1s ease",
}

const cssCarouselItemOnHover =
{
    "position": "relative",
    "background": "radial-gradient(#303030 1%, black 99%)",
    "width": "70%",
    "transition": "all 1s ease",
}

const cssBanner = 
{
    "position": "absolute",
    "top": "50%",
    "left": "50%",
    "transform": "translateX(-50%) translateY(-50%)",
}

class DolbyCarouselItem extends React.Component
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
        let linkStyle = (this.state.hover) ? cssCarouselItemOnHover : cssCarouselItem;
        return(
            <div onMouseEnter = { this.hoverHandler } 
                 onMouseLeave = { this.hoverHandler }
                 style = { linkStyle }
            >
                {this.state.hover ?
                    /* on hover display video */
                    <DolbyVideoJonbtron src = { this.props.src } />
                    :
                    /* on mouse leave display logo */
                    <img src    = { this.props.banner }
                        width  = "250px" 
                        height = "250px" 
                        style  = { cssBanner } />
                }
            </div>
        );
    }
}

export default DolbyCarouselItem;