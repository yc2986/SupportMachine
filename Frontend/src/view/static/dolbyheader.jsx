import React from 'react'
import { render } from 'react-dom'

/**
 * inline css style for navbar
 */
const cssNavbarStyle = 
{
    'color': 'white',
    'background': '#2C6195',
    'minHeight': '80px',
};

class DolbyHeader extends React.Component {

    render () {
        return (
            <nav className  = "navbar navbar-fixed-top navbar-full navbar-dark" 
                 style      = { cssNavbarStyle }>
                {/* Navbar LOGO & APP Title */} 
                <a className = "navbar-brand">
                    <img src    = "static/img/Dolby_Hrztl_White.png"
                         width  = "250" 
                         height = "45" />
                </a>
            </nav>
        );
    }
}

export default DolbyHeader;