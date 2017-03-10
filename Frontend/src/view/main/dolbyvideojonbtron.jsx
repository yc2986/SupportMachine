import React from "react"

/* inline css */
const cssJonbtron =
{
    "position": "relative",
}

const cssVideo =
{
    "width": "100%",
    "display": "block",
}

const cssOverlay =
{
    "position": "absolute",
    "top": "50%",
    "left": "50%",
    "transform": "translateX(-50%) translateY(-50%)",
    "zIndex": "1",
    "textAlign": "center",
    "color": "white",
    "fontFamily": "Consolas, Candara, Verdana",
}

class DolbyVideoJonbtron extends React.Component
{
    render() {
        //let playerState = "playsinline autoplay loop".concat(this.state.mute ? " mute" : "");
        return (
            <div style = { cssJonbtron }>
                <video className = "media-element"
                       style     = { cssVideo }
                       autoPlay  = "autoplay"
                       loop      = "loop">
                    <source src  = { this.props.src }
                            type = "video/webm" />
                </video>
                <div style = { cssOverlay }>
                    { this.props.children }
                </div>
            </div>
        );
    }
}

export default DolbyVideoJonbtron;