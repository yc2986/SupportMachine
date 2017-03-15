import React from "react"

/* inline css */
const cssJonbtron =
{
    "position": "relative",
    "marginBottom": "-1px",
    "background": "black",
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
    "fontFamily": "Verdana, Consolas, Candara",
}

class DolbyVideoJonbtron extends React.Component
{
    render() {
        return (
            <div style = { cssJonbtron }>
                <video className = "media-element"
                       style     = { cssVideo }
                       autoPlay  = "autoplay"
                       loop      = "loop"
                       muted     = "muted"
                       preload   = "auto">
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