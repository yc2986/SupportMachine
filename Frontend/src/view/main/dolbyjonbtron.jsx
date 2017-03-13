import React from "react"


const cssJonbtron =
{
    "width": "100%",
    "height": "200px",
    "background": "black",
    "paddingTop": "95px",
}

class DolbyJonbtron extends React.Component
{
    render() {
        return (
            <div className = "text-center"
                 style = { cssJonbtron }>
                { this.props.children }
            </div>
        );
    }
}

export default DolbyJonbtron;