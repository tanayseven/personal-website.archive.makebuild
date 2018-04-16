import React from 'react'

interface SocialSiteProps {icon: string, colour: string, link: string}

class SocialSiteLink extends React.Component<SocialSiteProps, {}> {
  render () {
    return (
      <span className="space-surrounding">
        <a
            className={"btn-floating btn-large waves-effect waves-light " + this.props.colour}
            href={this.props.link}
            target="_blank"
        >
            <i className={"fa fa-" + this.props.icon}/>
        </a>
      </span>
    )
  }
}

export default SocialSiteLink
