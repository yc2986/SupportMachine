import React from 'react'
import DolbyHeader from './static/dolbyheader.jsx'

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
            </div>
        );
    }
}

export default Index;