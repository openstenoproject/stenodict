import React, { Component, PropTypes } from 'react'
import { Link } from 'react-router'
import { Col, Button, Glyphicon } from 'react-bootstrap'
import Markdown from './Markdown'
import { LinkContainer } from 'react-router-bootstrap'

class DictionaryItem extends Component {
  render() {
    const { dictionary } = this.props
    const dictUrl = `dictionary/${dictionary.filename}`
    const dictName = dictionary.name
    const dictAuthor = dictionary.author
    return (
      <LinkContainer to={dictUrl}>
      <tr style={{cursor: 'pointer'}}>
        <td>
          <h4 className="dictionary-name">{ dictName }</h4>
          <small className="author"> by { dictAuthor }</small><br/>{ `${dictionary.what}` }
          <Glyphicon glyph="chevron-right" className="pull-right"/>
          </td>
        </tr>
      </LinkContainer>
        )
      }
    }

DictionaryItem.PropTypes = { dictionary: PropTypes.object }

export default DictionaryItem
