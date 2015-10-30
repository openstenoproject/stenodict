import React, { Component, PropTypes } from 'react'
import { Link } from 'react-router'
import { Col, Button, Glyphicon } from 'react-bootstrap'
import Markdown from './Markdown'
import { LinkContainer } from 'react-router-bootstrap'

class DictionaryItem extends Component {
  render() {
    const { dictionary } = this.props
    const dictUrl = `dictionary/${dictionary.filename}`
    const dictName = `${dictionary.name}`
    return (
      <LinkContainer to={dictUrl}>
      <tr style={{cursor: 'pointer'}}>
        <td>
          <b>{ dictName }</b><br/>{ `${dictionary.what}` }
          <Glyphicon glyph="chevron-right" className="pull-right"/>
          </td>
        </tr>
      </LinkContainer>
        )
      }
    }

DictionaryItem.PropTypes = { dictionary: PropTypes.object }

export default DictionaryItem
