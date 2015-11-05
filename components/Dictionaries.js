import React, { Component, PropTypes } from 'react'
import { Table } from 'react-bootstrap'
import DictionaryItem from './DictionaryItem'

class Dictionaries extends Component {
  render() {
    const { dictionaries, filtered } = this.props
    let tableContent
    if (dictionaries.fetching) {
      tableContent = (<tr><td colSpan="2">Loading dictionaries...</td></tr>)
    } else if (filtered.length >= 1) {
      let list = dictionaries.list
      tableContent = filtered
        .map(x =>
          (<DictionaryItem key={x} dictionary={list[x]} />)
        )
    } else if (filtered.length === 0 &&
               Object.keys(dictionaries.list).length > 0) {
      return (<em>No dictionaries match all the selected filters.</em>)
    } else {
      // This should not show up
      // because dictionaries.list shouldn't
      // be handed in empty.
      return (<em>No dictionaries found.</em>)
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

Dictionaries.propTypes = { dictionaries: PropTypes.object.isRequired
                         , filtered: PropTypes.array.isRequired
                         }

export default Dictionaries
