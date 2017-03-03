import React from "react"

//inline css style
const cssHeader = 
{
    "color": "white",
    "background": "#2C6195",
    "minHeight": "80px",
};

const cssHeaderTitle =
{
    fontFamily: "Monaco, Consolas, Arial",
}

class DolbyHeader extends React.Component {

    render () {
        return (
            <nav className  = "navbar navbar-fixed-top navbar-full navbar-dark" 
                 style      = { cssHeader }>
                {/* logo */} 
                <div className = "navbar-brand">
                    <img src    = "static/img/Dolby_Hrztl_White.png"
                         width  = "250" 
                         height = "45" />
                </div>
                {/* title */}
                <div style = { cssHeaderTitle }>
                    <h2>Support Machine</h2>
                </div>
            </nav>
        );
    }
}

export default DolbyHeader;