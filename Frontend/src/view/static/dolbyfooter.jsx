import React from "react"
import Social from "./social.jsx"

//inline css style
const cssFooter = 
{
    "position": "absolute",
    "bottom": "0",
    "width": "100%",
    "height": "350px",
    "paddingTop": "25px",
    "color": "white",
    "background": "#2C6195",
};

const cssTable =
{
    "tableLayout": "fixed",
    "border": "none",
    "width": "80%",
    "height": "275px",
    "margin": "20px 10% 0 15%",
    "fontFamily": "Consolas, Candara, Verdana",
    "textAlign": "left",
}

const cssTableHeader =
{
    "fontSize": "18px",
    "fontWeight": "bold",
}

class DolbyFooter extends React.Component {

    render () {
        return (
            <nav className = "text-center center-block" 
                 style     = { cssFooter }>
                <Social href="https://www.facebook.com/dolby/" icon="fa-facebook" />
                <Social href="https://twitter.com/dolby" icon="fa-twitter" />
                <Social href="https://mp.weixin.qq.com/s/ZG-iaDc1q74hdR_I-LWE6w" icon="fa-weixin" />
                <Social href="https://weibo.com/dolbychina" icon="fa-weibo" />
                <table style = { cssTable }>
                    <tbody>
                        <tr style = { cssTableHeader }>
                            <td>Dolby</td>
                            <td>Professional</td>
                            <td>Who We Are</td>
                            <td>Investors</td>
                        </tr>
                        <tr>
                            <td>Cinema</td>
                            <td>AV Installers and Retailers</td>
                            <td>Leadership</td>
                            <td>Company Financials</td>
                        </tr>
                        <tr>
                            <td>Home Theater</td>
                            <td>Broadcast</td>
                            <td>Worldwide Offices</td>
                            <td>Corporate Governance</td>
                        </tr>
                        <tr>
                            <td>Mobile</td>
                            <td>Cinema</td>
                            <td>Environmental Commitment</td>
                            <td>Stock Information</td>
                        </tr>
                        <tr>
                            <td>Office</td>
                            <td>Content Services</td>
                            <td>Press Releases</td>
                            <td>Investor Resources</td>
                        </tr>
                        <tr>
                            <td></td>
                            <td>Game Development</td>
                        </tr>
                        <tr>
                            <td></td>
                            <td>PC and Mobile</td>
                        </tr>
                        <tr>
                            <td></td>
                            <td>Streaming</td>
                        </tr>
                    </tbody>
                </table>
            </nav>
        );
    }
}

export default DolbyFooter;