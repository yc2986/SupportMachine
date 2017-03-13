import React from "react"
import Social from "./social.jsx"
import DolbyFooterLink from "./dolbyfooterlink.jsx"

//inline css style
const cssFooter = 
{
    "position": "absolute",
    "bottom": "-500px",
    "width": "100%",
    "height": "500px",
    "color": "white",
    "background": "black",
};

const cssTable =
{
    "tableLayout": "fixed",
    "border": "none",
    "width": "80%",
    "height": "400px",
    "margin": "15px 10% 0 15%",
    "fontFamily": "Verdana, Consolas, Candara",
    "textAlign": "left",
}

const cssTableHeader =
{
    "fontSize": "22px",
    "fontWeight": "bold",
}

class DolbyFooter extends React.Component {

    render () {
        return (
            <nav className = "text-center center-block" 
                 style     = { cssFooter }>
                <table style = { cssTable }>
                    <tbody>
                        <tr style = { cssTableHeader }>
                            <td>Dolby</td>
                            <td>Professional</td>
                            <td>Who We Are</td>
                            <td>Investors</td>
                        </tr>
                        <tr>
                            <td>
                                <DolbyFooterLink 
                                    href="https://www.dolby.com/us/en/cinema/index.html"
                                    text="Cinema" 
                                />
                            </td>
                            <td>
                                <DolbyFooterLink 
                                    href="https://www.dolby.com/us/en/professional/av-installers/industry.html"
                                    text="AV Installers and Retailers" 
                                />
                            </td>
                            <td>
                                <DolbyFooterLink 
                                    href="https://www.dolby.com/us/en/about/leadership/senior-management-officers.html"
                                    text="Leadership" 
                                /> 
                            </td>
                            <td>
                                <DolbyFooterLink 
                                    href="http://investor.dolby.com/releases-financial.cfm"
                                    text="Company Financials"
                                />
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <DolbyFooterLink 
                                    href="https://www.dolby.com/us/en/home/index.html"
                                    text="Home Theater"
                                />
                            </td>
                            <td>
                                <DolbyFooterLink 
                                    href="https://www.dolby.com/us/en/professional/broadcast/industry.html"
                                    text="Broadcast"
                                />
                            </td>
                            <td>
                                <DolbyFooterLink 
                                    href="https://www.dolby.com/us/en/about/contact-us/dolby-offices-worldwide.html"
                                    text="Worldwide Offices"
                                />
                            </td>
                            <td>
                                <DolbyFooterLink 
                                    href="https://www.dolby.com/us/en/about/investors/corporate-governance.html"
                                    text="Corporate Governance"
                                />
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <DolbyFooterLink 
                                    href="https://www.dolby.com/us/en/mobile/index.html"
                                    text="Mobile"
                                />
                            </td>
                            <td>
                                <DolbyFooterLink 
                                    href="https://www.dolby.com/us/en/professional/cinema/industry.html"
                                    text="Cinema"
                                />
                            </td>
                            <td>
                                <DolbyFooterLink 
                                    href="https://www.dolby.com/us/en/about/environmental-commitment.html"
                                    text="Environmental Commitment"
                                />
                            </td>
                            <td>
                                <DolbyFooterLink 
                                    href="https://www.dolby.com/us/en/about/investors/stock-information.html"
                                    text="Stock Information"
                                />
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <DolbyFooterLink 
                                    href="https://www.dolby.com/us/en/work/index.html"
                                    text="Office"
                                />
                            </td>
                            <td>
                                <DolbyFooterLink 
                                    href="https://www.dolby.com/us/en/professional/cinema/industry/content-services.html"
                                    text="Content Services"
                                />
                            </td>
                            <td>
                                <DolbyFooterLink 
                                    href="https://www.dolby.com/us/en/about/news-and-events/press-releases.html"
                                    text="Press Releases"
                                />
                            </td>
                            <td>
                                <DolbyFooterLink 
                                    href="https://www.dolby.com/us/en/about/investors/investor-resources.html"
                                    text="Investor Resources"
                                />
                            </td>
                        </tr>
                        <tr>
                            <td></td>
                            <td>
                                <DolbyFooterLink 
                                    href="https://www.dolby.com/us/en/professional/games/industry.html"
                                    text="Game Development"
                                />
                            </td>
                        </tr>
                        <tr>
                            <td></td>
                            <td>
                                <DolbyFooterLink 
                                    href="https://www.dolby.com/H5TwoColumnWideLeft.aspx?pageid=1381"
                                    text="PC and Mobile"
                                />
                            </td>
                        </tr>
                        <tr>
                            <td></td>
                            <td>
                                <DolbyFooterLink 
                                    href="https://www.dolby.com/us/en/professional/streaming/industry.html"
                                    text="Streaming"
                                />
                            </td>
                        </tr>
                    </tbody>
                </table>
            </nav>
        );
    }
}

export default DolbyFooter;