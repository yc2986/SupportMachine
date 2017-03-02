import React from 'react'
import { render } from 'react-dom'

class Index extends React.Component
{
    render() {
        return <p>This is your Support Machine!</p>
    }
}

render(<Index/>, document.getElementById('index'));