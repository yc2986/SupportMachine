import React from "react"
import DolbyCarouselItem from "./dolbycarouselitem.jsx"

const cssCarousel = 
{
    "height": "360px",
    "display": "flex",
    "background": "black",
}

class DolbyCarousel extends React.Component
{
    render() {
        return (
            <div style = { cssCarousel }>
                {this.props.sources.map(function(item, id) {
                    return <DolbyCarouselItem banner = { item.banner } 
                                              src    = { item.src } />
                })}
            </div>
        );
    }
}

export default DolbyCarousel;