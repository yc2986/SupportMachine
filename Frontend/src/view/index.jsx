import React from "react"
import DolbyHeader from "./static/dolbyheader.jsx"
import DolbyFooter from "./static/dolbyfooter.jsx"
import DolbyVideoJonbtron from "./main/dolbyvideojonbtron.jsx"

const cssReferenceEntryPoint = 
{
    "position": "relative",
}

const cssBody = 
{
    "marginTop": "80px",
}

class Index extends React.Component
{
    render() {
        return (
            <div style = { cssReferenceEntryPoint }>
                <DolbyHeader />
                <div style = { cssBody }>
                    <DolbyVideoJonbtron 
                        src = "http://download.dolby.com/us/en/technology/Dolby-Atmos-Ambient-Space-Video.mp4"
                    >
                        <div>
                            <img src   = "static/resources/img/Dolby_Hrztl_White.png"
                                width  = "800" 
                                height = "150" />
                            <img src   = "static/resources/img/HearEveryDimension_white.png"
                                width  = "900" 
                                height = "200" />
                            {/*<h1>Service Machine</h1>*/}
                        </div>
                    </DolbyVideoJonbtron>
                    <DolbyVideoJonbtron src = "https://dolby.box.com/shared/static/mearbwtvcv3qjlllpyggzrgdps7usnhu.mp4" />
                    <DolbyVideoJonbtron src = "https://dolby.box.com/shared/static/ny69jf2le8koizyd7iobpsib4naslovi.mp4" />
                </div>
                <DolbyFooter />
            </div>
        );
    }
}

export default Index;