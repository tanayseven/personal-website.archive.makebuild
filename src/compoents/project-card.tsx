import React from 'react'

interface ProjectCardProps {title: string, image: string|null, liveLink: string|null, codeLink: string|null}

class ProjectCard extends React.Component<ProjectCardProps, {}> {
  render () {
    return (
      <div className="row">
        <div className="card">
          <div className="card-image">
            <img src={this.props.image}/>
          </div>
          <div className="card-content">
            <span className="card-title">{this.props.title}</span>
            {this.props.children}
          </div>
          <div className="card-action">
            {(()=> {
              if (this.props.codeLink != null)
                return <a href={this.props.codeLink}>Code</a>
            })()}
            {(()=> {
              if (this.props.liveLink != null)
                return <a href={this.props.liveLink}>Live Demo</a>
            })()}
          </div>
        </div>
      </div>
    )
  }
}

export default ProjectCard
