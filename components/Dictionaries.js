import React, { Component, PropTypes } from 'react'
import Dictionary from './Dictionary'

class Dictionaries extends Component {
  render() {
    const { dictionaries } = this.props
    return (
      <ul>
        { dictionaries.list.map(x => (<Dictionary key={x.filename} dictionary={x} />)) }
      </ul>
    )
  }
}

Dictionaries.propTypes = { dictionaries: React.PropTypes.object.isRequired
                         }

export default Dictionaries
