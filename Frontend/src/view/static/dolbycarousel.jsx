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
        const sources = this.props.sources;
        return (
            <div style = { cssCarousel }>
                {sources.map(function(item, id) {
                    return <DolbyCarouselItem banner = { item.banner } 
                                              src    = { item.src } />
                })}
            </div>
        );
    }
}

export default DolbyCarousel;