import React from "react"

//inline css style
const cssHeader = 
{
    "color": "white",
    "background": "black",
    "height": "80px",
};

const cssHeaderTitle =
{
    fontFamily: "Verdana, Consolas, Candara",
}

class DolbyHeader extends React.Component {

    render () {
        return (
            <nav className  = "navbar navbar-fixed-top navbar-full navbar-dark" 
                 style      = { cssHeader }>
                {/* logo */} 
                <div className = "navbar-brand">
                    <img src    = "static/resources/img/Dolby_symbol_White.png"
                         width  = "70" 
                         height = "45" />
                </div>
            </nav>
        );
    }
}

export default DolbyHeader;