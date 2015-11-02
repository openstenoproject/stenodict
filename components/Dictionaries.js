import React, { Component, PropTypes } from 'react'
import { Table } from 'react-bootstrap'
import DictionaryItem from './DictionaryItem'

class Dictionaries extends Component {
  render() {
    const { dictionaries } = this.props
    let tableContent
    if (dictionaries.fetching) {
      tableContent = (<tr><td colSpan="2">Loading dictionaries...</td></tr>)
    } else {
      let list = dictionaries.list
      tableContent = Object.keys(list).map(x =>
        (<DictionaryItem key={x} dictionary={list[x]} />))
    }

    return (
      <Table striped bordered hover>
        <tbody>
          { tableContent }
        </tbody>
      </Table>
    )
  }
}

Dictionaries.propTypes = { dictionaries: React.PropTypes.object.isRequired
                         }

export default Dictionaries
