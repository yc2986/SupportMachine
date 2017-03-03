import React from "react"
import Social from "./social.jsx"

//inline css style
const cssFooter = 
{
    "color": "white",
    //"background": "#2C6195",
    "position": "fixed",
    "bottom": "0"
};

class DolbyFooter extends React.Component {

    render () {
        return (
            <div className = "navbar-fixed-bottom text-center center-block" 
                 style     = { cssFooter }>
                <Social href="https://www.facebook.com/bootsnipp" icon="fa-facebook" />
                <Social href="https://twitter.com/bootsnipp" icon="fa-twitter" />
                <Social href="https://plus.google.com/+Bootsnipp-page" icon="fa-weixin" />
                <Social href="https://plus.google.com/+Bootsnipp-page" icon="fa-weibo" />
            </div>
        );
    }
}

export default DolbyFooter;