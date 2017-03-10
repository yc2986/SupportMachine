import React from "react"

//inline css style
const cssHeader = 
{
    "color": "white",
    "background": "#2C6195",
    "height": "80px",
};

const cssHeaderTitle =
{
    fontFamily: "Consolas, Candara, Verdana",
}

class DolbyHeader extends React.Component {

    render () {
        return (
            <nav className  = "navbar navbar-fixed-top navbar-full navbar-dark" 
                 style      = { cssHeader }>
                {/* logo */} 
                <div className = "navbar-brand">
                    <img src    = "static/img/Dolby_symbol_White.png"
                         width  = "60" 
                         height = "45" />
                </div>
            </nav>
        );
    }
}

export default DolbyHeader;