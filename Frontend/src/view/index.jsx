import React from "react"
import DolbyHeader from "./static/dolbyheader.jsx"
import DolbyFooter from "./static/dolbyfooter.jsx"

const cssBody = 
{
    "marginTop": "80px"
}

class Index extends React.Component
{
    render() {
        return (
            <div>
                <DolbyHeader />
                <div style = { cssBody }>
                    <h1>This is your Support Machine!</h1>
                </div>
                <DolbyFooter />
            </div>
        );
    }
}

export default Index;